document.addEventListener('DOMContentLoaded', () => {
    const friendItems = document.querySelectorAll('.friend-item'); // Friend list items
    const chatContent = document.querySelector('.chat-content'); // Right column for messages
    const chatInput = document.querySelector('.chat-input input'); // Input field for new message
    const sendButton = document.querySelector('.chat-input button'); // Send button
    const chatHeader = document.querySelector('.chat-header h3'); // Chat header for title
    let currentUserUUID = ''; // Track the selected friend's UUID

    // Function to scroll chat to the bottom
    function scrollChatToBottom() {
        chatContent.scrollTop = chatContent.scrollHeight;
    }

    // Function to load chat messages
    function loadChat(userUUID) {
        fetch(`/chats/messages/${userUUID}/`)
            .then(response => response.json())
            .then(data => {
                chatContent.innerHTML = ''; // Clear the previous chat
                currentUserUUID = userUUID; // Update the current user UUID

                // Update chat header with chat name
                chatHeader.innerText = data.chat_name;

                // Load author and recipient messages
                const authorAvatarURL = data.author_avatar_url;
                const recipientAvatarURL = data.recipient_avatar_url;
                const authorMessages = data.author_messages;
                const recipientMessages = data.recipient_messages;

                // Merge and sort messages by time
                const allMessages = [];
                authorMessages.forEach(([content, createdAt]) => {
                    allMessages.push({ content, createdAt, sender: 'author' });
                });
                recipientMessages.forEach(([content, createdAt]) => {
                    allMessages.push({ content, createdAt, sender: 'recipient' });
                });
                allMessages.sort((a, b) => new Date(a.createdAt) - new Date(b.createdAt)); // Sort by time

                // Render messages
                allMessages.forEach(msg => {
                    const messageDiv = document.createElement('div');
                    messageDiv.classList.add('message', msg.sender === 'author' ? 'message-right' : 'message-left');

                    const avatarImg = document.createElement('img');
                    avatarImg.src = msg.sender === 'author' ? authorAvatarURL : recipientAvatarURL;
                    avatarImg.classList.add('avatar'); // Add the 'avatar' class for styling

                    const messageText = document.createElement('p');
                    messageText.innerText = msg.content;

                    messageDiv.appendChild(avatarImg); // Add avatar to message
                    messageDiv.appendChild(messageText); // Add message content
                    chatContent.appendChild(messageDiv); // Append the message div to chat content
                });

                scrollChatToBottom(); // Scroll to the bottom of chat
            })
            .catch(error => {
                console.error('Error loading chat:', error);
            });
    }

    // Function to refresh the current chat every 5 seconds
    function refreshChat() {
        if (currentUserUUID) {
            loadChat(currentUserUUID);
        }
    }
    setInterval(refreshChat, 15000); // Set refresh interval to 15 seconds

    // Event listener for friend item click
    friendItems.forEach(item => {
        item.addEventListener('click', () => {
            const userUUID = item.dataset.userUuid; // Get the friend's UUID
            loadChat(userUUID); // Load chat for the selected friend
        });
    });

    // Send message functionality
    sendButton.addEventListener('click', () => {
        const messageContent = chatInput.value.trim();

        if (messageContent !== '') {
            fetch(`/chats/messages/${currentUserUUID}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value // CSRF token for Django
                },
                body: new URLSearchParams({ content: messageContent })
            })
            .then(response => {
                if (response.status === 204) {
                    // Message sent successfully, reload chat
                    chatInput.value = ''; // Clear input field
                    loadChat(currentUserUUID); // Reload the chat to reflect the new message
                }
            })
            .catch(error => {
                console.error('Error sending message:', error);
            });
        }
    });
});
