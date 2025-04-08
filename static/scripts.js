document.getElementById('reimbursementForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const form = new FormData(this);
    const messageElement = document.getElementById('message');

    fetch('http://localhost:5000/api/receipts/submit', {
        method: 'POST',
        body: form
    })
    .then(response => response.json())
    .then(data => {
        messageElement.textContent = data.message || 'Receipt submitted successfully!';
    })
    .catch(error => {
        messageElement.textContent = 'Error submitting receipt.';
        console.error('Error:', error);
    });
});
