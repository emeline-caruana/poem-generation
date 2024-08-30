# poem-generation



## Name
Génération de poèmes 

## Description
Ce projet est un projet de fin de formation LLM Ops avec Datascientest. 
Il porte sur la génération de poèmes à partir d'un thème en anglais. 

## Rapport de projet
Le rapport de projet est disponible en format PDF à la racine du projet GitLab

## Architecture du repo
Le repo a deux dossiers principaux : application et finetuning.

Le dossier finetuning est composé de quatres dossiers :
 - dataset : contient tout le dataset en format .zip ainsi que les .json utilisés pour le fine-tuning
 - fine-tuning : contient les fichiers .ipynb créés pour le fine-tuning
 - chains-evaluation : contient les fichiers .ipynb créés pour tester les chaînes de LLM et évaluer les sorties du modèle fine-tuned
 - models : contient les dossiers avec les différentes versions du modèle fine-tuned, comme dans le Comet Model Registry 

Le dossier application est composé de deux dossiers:
 - front : contient les fichiers .html, .css et .js pour la partie graphique de l'application
 - back : contient le fichier .py qui permet de faire tourner l'application ainsi qu'un ficher .ipynb pour tester l'application


## Usage
Pour tester le projet, il suffit de se mettre dans le dossier application et exécuter cette commande : ```python3 /back/app.py```
Et ensuite, il suffit de se connecter au local host par : ```http://localhost:5050```

## Authors 
Emeline Caruana

## Project status
Le projet est presque terminé, la seule partie qui n'est pas totalement finie est celle de la création d'images docker et l'orchestration avec kubernetes. 

## Liens externes qui concerne le projet
HuggingFace Hub : https://huggingface.co/emeline-caruana/t5-poem-gen
Comet ML projet : 
    1e FT : https://www.comet.com/emeline-caruana/poem-gen-ft-v2
    2e FT : https://www.comet.com/emeline-caruana/poem-gen-ft-v2-2
Comet ML model registry : https://www.comet.com/emeline-caruana/model-registry/t5-finetuned
Comet ML chains : https://www.comet.com/emeline-caruana/poem-generation-chains-comet
