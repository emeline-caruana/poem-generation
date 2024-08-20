document.getElementById('apiForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const data = document.getElementById('data').value;

    fetch('http://34.252.129.48:5000/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ data: data })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
		var  texte = JSON.stringify(data["poem"])
        var formattedData = texte.replaceAll("\\n", '<br>');
		console.log('Success:', texte);
        document.getElementById('response').innerHTML = formattedData;
    })
    .catch((error) => {
        console.error('Error:', error);
        document.getElementById('response').textContent = 'Erreur lors de l\'envoi des données.';
    });
});
