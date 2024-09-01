document.addEventListener('DOMContentLoaded', function() {
    const registerForm = document.getElementById('registerForm');
    const errorMessage = document.getElementById('errorMessage');

    registerForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission

        const formData = new URLSearchParams(new FormData(registerForm)).toString();

        fetch('/authz/register/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: formData
        })
        .then(response => {
            if (response.status === 201) {
                // Handle successful registration
                window.location.href = '/authz/login/';
            } else {
                return response.json(); // Process JSON response for errors
            }
        })
        .then(data => {
            if (data && data.error) {
                errorMessage.textContent = data.error;
                errorMessage.style.display = 'block';
            }
        })
        .catch(error => {
            console.error('Error:', error);
            errorMessage.textContent = 'An error occurred. Please try again.';
            errorMessage.style.display = 'block';
        });
    });
});
