document.getElementById('apiForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const topic = document.getElementById('data').value;

    // Use the backend service name defined in docker-compose.yaml
    const backendUrl = 'http://backend:5050';

    fetch(`${backendUrl}/predict`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: topic })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);

        var poemText = data.final_poem || 'No poem generated.';

        var formattedData = poemText.replace(/\n/g, '<br>');

        document.getElementById('response').innerHTML = formattedData;
    })
    .catch((error) => {
        console.error('Error:', error);
        document.getElementById('response').textContent = 'Erreur lors de l\'envoi de la requête.';
    });
});

