document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.getElementById('loginForm');
    const errorMessage = document.getElementById('errorMessage');

    loginForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission
        const formData = new URLSearchParams(new FormData(loginForm)).toString();

        fetch('/authz/login/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                errorMessage.textContent = data.error;
                errorMessage.style.display = 'block';
            } else {
                // Handle successful login, e.g., redirect to another page
                localStorage.setItem('JWT', data.token);
                window.location.href = '/';
            }
        })
        .catch(error => {
            console.error('Error:', error);
            errorMessage.textContent = 'An error occurred. Please try again.';
            errorMessage.style.display = 'block';
        });
    });
});
