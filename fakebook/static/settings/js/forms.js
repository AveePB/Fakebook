// Handle form submissions
const forms = document.querySelectorAll('.form-container');

forms.forEach(form => {
    form.addEventListener('submit', function(event) {
        event.preventDefault();

        const url = form.action;
        const method = form.method.toUpperCase();
        const formData = new FormData(form);

        // Debugging: Log the method, URL, and form data
        console.log("Submitting form...");
        console.log(`Method: ${method}`);
        console.log(`URL: ${url}`);
        console.log("Form data:", formData);

        fetch(url, {
            method: method,
            body: method === 'POST' ? formData : null,
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': formData.get('csrfmiddlewaretoken') // Adjust if CSRF protection is implemented
            }
        })
        .then(response => {
            console.log(`Response status: ${response.status}`); // Log the status code
            return response.text().then(text => {
                let data = {};
                try {
                    data = JSON.parse(text);
                } catch {
                    data.message = text;
                }
                return { status: response.status, message: data.message };
            });
        })
        .then(result => {
            console.log("Result:", result); // Log the response body
            const messageBoxId = form.getAttribute('data-message-box');
            const messageBox = document.getElementById(messageBoxId);

            if (messageBox) {
                // Clear previous classes
                messageBox.classList.remove('success', 'error');
                
                // Add new class based on result status
                if (result.status === 204 || result.status == 200) {
                    messageBox.classList.add('success');
                    messageBox.innerHTML = result.message || 'Operation completed.';
                    setTimeout(() => {
                        window.location.reload();
                    }, 500);
                } else {
                    messageBox.classList.add('error');
                    messageBox.innerHTML = result.message || 'Operation failed.';
                }
                
                // Clear form data
                form.reset();
            }
        })
        .catch(error => {
            console.error('Error:', error);
            const messageBoxId = form.getAttribute('data-message-box');
            const messageBox = document.getElementById(messageBoxId);
            if (messageBox) {
                messageBox.classList.remove('success', 'error');
                messageBox.classList.add('error');
                messageBox.innerHTML = 'An error occurred. Please try again.';
            }
        });
    });
});
