function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Delete buttons
const deleteButtons = document.querySelectorAll('.delete-btn');

deleteButtons.forEach(deleteButton => {
    deleteButton.addEventListener('click', function(event) {
        event.preventDefault();

        // Retrieve the data attributes (URL, item ID, and message box ID) from the button
        const url = deleteButton.getAttribute('data-url');
        const messageBoxId = deleteButton.getAttribute('data-message-box');
        const messageBox = document.getElementById(messageBoxId);
        const csrftoken = getCookie('csrftoken');

        // Confirmation dialog before deletion
        if (confirm(`Are you sure you want to delete it?`)) {
            fetch(url, {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken,
                }
            })
            .then(response => response.text().then(text => {
                let data = {};
                try {
                    data = JSON.parse(text);
                } catch {
                    data.message = text;
                }
                return { status: response.status, message: data.message };
            }))
            .then(result => {
                // Clear previous classes
                messageBox.classList.remove('success', 'error');

                // Display the result
                messageBox.style.display = 'block';
                if (result.status === 204 || result.status === 200) {
                    messageBox.classList.add('success');
                    messageBox.innerHTML = result.message || `Successfully deleted.`;
                    setTimeout(() => {
                        window.location.reload();
                    }, 500);
                } else {
                    messageBox.classList.add('error');
                    messageBox.innerHTML = result.message || `Failed to delete.`;
                }
            })
            .catch(error => {
                console.error('Error:', error);
                messageBox.classList.remove('success');
                messageBox.classList.add('error');
                messageBox.style.display = 'block';
                messageBox.innerHTML = 'An error occurred. Please try again.';
            });
        }
    });
});
