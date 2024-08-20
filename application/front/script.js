document.getElementById('apiForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const topic = document.getElementById('data').value;

    fetch('/predict', {  // Changed to relative URL
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: topic })  // Corrected the key to match Flask endpoint
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        
        // Access the final_poem from the response
        var poemText = data.final_poem || 'No poem generated.';

        // Replace newlines with <br> for HTML display
        var formattedData = poemText.replace(/\n/g, '<br>');  

        document.getElementById('response').innerHTML = formattedData;
    })
    .catch((error) => {
        console.error('Error:', error);
        document.getElementById('response').textContent = 'Erreur lors de l\'envoi des données.';
    });
});
