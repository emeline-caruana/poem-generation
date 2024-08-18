## Imports pour Flask
from flask import Flask, request, jsonify
from flask_cors import CORS

## Imports pour les transformers
from transformers import T5Tokenizer, T5ForConditionalGeneration

## Imports pour langchain et l'agent
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.output_parsers import StrOutputParser

## Imports pour récupérer le modèle fine-tuned
import comet_ml
from comet_ml import API
from comet_ml import Experiment

## Imports pour le RAG
import pinecone
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore

## Initialisation de Flask
app = Flask(__name__)
CORS(app)

## Téléchargement de mon modèle fine-tuned et son tokeniser
t5_model = T5ForConditionalGeneration.from_pretrained(folder_path)
t5_tokenizer = T5Tokenizer.from_pretrained(folder_path)

## Initialisation Google Gen AI
google_llm = GoogleGenerativeAI(model="gemini-pro", google_api_key="AIzaSyDI4gpwnwFsta6WkVsnRrcJxzZzgHHSunE")

## Mémoire
memory_store = []

## Modèle d'embeddings
embeddings = HuggingFaceEmbeddings(model_name= "mixedbread-ai/mxbai-embed-large-v1",
                                   model_kwargs= {'device': 'cpu'},
                                   encode_kwargs= {'normalize_embeddings': False})

## Initialisation Pinecone
pc = pinecone.Pinecone(api_key='a1ae148e-e273-4cc8-895e-b1135d91b65f')
index = pc.Index('poem-gen-rag')
vector_store = PineconeVectorStore(index=index, embedding=embeddings, text_key="text")

## RAG
def retrieve_context_from_pinecone(topic):
    ## Encoding du sujet en utilisant le même modèle d'embedding que celui utilisé pour Pinecone
    embedding = generate_embedding_for_topic(topic)
    
    ## Interrogation de Pinecone pour des textes similaires
    query_result = index.query(vector=embedding, top_k=3, namespace='poem-gen-rag')
    ## Combinaison des résultats en une seule chaîne de contexte
    context = ' '.join([match['metadata']['text'] for match in query_result['matches']])
    return context if context else "No additional context available."


def generate_embedding_for_topic(topic):    
    embedd = embeddings.embed_query(topic)
    print(len(embedd))
    print(embedd)
    return embedd


@app.route('/predict', methods=['POST'])
## Final poem generation
def predict(request, topic):
    data = request
    for item in memory_store:
        if item['topic'] == topic:
            return {
                'status': 'success',
                'topic': topic,
                'poem': item['poem'],
                'from_memory': True
            }
    
    prompt = f"Generate a short poem about this topic: {topic}"
    inputs = t5_tokenizer.encode(prompt, return_tensors="pt")
    t5_output = t5_model.generate(inputs, max_length=50, num_return_sequences=1)
    t5_poem = t5_tokenizer.decode(t5_output[0], skip_special_tokens=True)
    
    context = retrieve_context_from_pinecone(topic)
    
    final_prompt_template = (
        "Here is a poem generated about {topic}: {poem}. "
        "With the following additional context: {context}. "
        "Please refine and improve this poem."
    )
    
    prompt_template = PromptTemplate(
        input_variables=["topic", "poem", "context"],
        template=final_prompt_template
    )
    
    chain = prompt_template | google_llm | StrOutputParser()
    final_poem = chain.invoke({"topic": topic, "poem": t5_poem, "context": context})
    
    memory_store.append({
        'topic': topic,
        'poem': final_poem
    })

    return {
        'status': 'success',
        'topic': topic,
        'initial_poem': t5_poem,
        'final_poem': final_poem,
        'from_memory': False
    }



@app.route('/get_poem', methods=['POST'])
def get_poem():
    data = request.json
    topic = data.get('text')
    
    ## Récupération du poème dans la mémoire
    for item in memory_store:
        if item['topic'] == topic:
            return jsonify({
                'status': 'success',
                'topic': topic,
                'poem': item['poem'],
                'from_memory': True
            })
    
    return jsonify({
        'status': 'error',
        'message': 'Poem not found for the given topic.'
    })
    


@app.route('/', methods=['GET'])
def index():
    return "Welcome to the Poem Generator by Emeline !"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
