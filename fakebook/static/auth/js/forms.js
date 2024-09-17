// Ensures that listener is set after document is loaded
document.addEventListener('DOMContentLoaded', function () {
    console.log("DOM fully loaded and parsed.");

    const form = document.querySelector('form');
    if (!form) {
        console.error("Form not found");
        return;  // Stop if form is not found
    }

    const messageBoxId = form.getAttribute('message-box');  // Fetch the message-box ID from the form's attribute
    const messageBox = document.getElementById(messageBoxId);  // Use the correct ID from the form

    if (!messageBox) {
        console.error("Message box not found");
    }

    form.addEventListener('submit', function (event) {
        event.preventDefault();  // Prevent the default form submission
        console.log("Form submission intercepted");

        const xhr = new XMLHttpRequest();
        const formData = new FormData(form);

        xhr.open(form.method, form.action);
        console.log("XHR Request opened: ", form.method, form.action);

        xhr.onload = function () {
            console.log("XHR Request onload triggered. Status: ", xhr.status);

            try {
                const result = JSON.parse(xhr.responseText);
                console.log("Parsed response: ", result);
                
                if (xhr.status >= 200 && xhr.status < 300) {
                    messageBox.textContent = `Success: ${result.message}`;
                    messageBox.className = 'message-box success'; // Add success class
                    setTimeout(function () {
                        location.reload();
                    }, 500); // 500 ms delay
                } else {
                    messageBox.textContent = `Error: ${result.message}`;
                    messageBox.className = 'message-box error'; // Add error class
                }
            } catch (error) {
                console.error("Failed to parse response: ", xhr.responseText);
            }
        };

        xhr.onerror = function () {
            console.error("XHR Request failed.");
            messageBox.textContent = 'An error occurred.';
            messageBox.className = 'message-box error'; // Add error class
        };

        xhr.send(formData);
        console.log("XHR request sent.");
    });
});
