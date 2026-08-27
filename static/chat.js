document.addEventListener('DOMContentLoaded', function() {
    const chatWidget = document.getElementById('chat-widget');
    const chatToggle = document.getElementById('chat-toggle');
    const closeChat = document.getElementById('close-chat');
    const chatForm = document.getElementById('chat-form');
    const chatInput = document.getElementById('chat-input');
    const chatMessages = document.getElementById('chat-messages');

    // Toggle Chat Window
    function toggleChat() {
        chatWidget.classList.toggle('active');
        if (chatWidget.classList.contains('active')) {
            chatInput.focus();
        }
    }

    chatToggle.addEventListener('click', toggleChat);
    closeChat.addEventListener('click', toggleChat);

    // Close on click outside
    document.addEventListener('click', function(event) {
        if (!chatWidget.contains(event.target) && !chatToggle.contains(event.target) && chatWidget.classList.contains('active')) {
            toggleChat();
        }
    });

    // Handle Message Submission
    chatForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const message = chatInput.value.trim();
        if (!message) return;

        // Add User Message
        addMessage(message, 'user');
        chatInput.value = '';

        // Show Loading (Simple dots)
        const loadingId = addMessage('...', 'bot', true);

        // Fetch Response
        fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: message }),
        })
        .then(response => response.json())
        .then(data => {
            removeMessage(loadingId);
            if (data.response) {
                addMessage(data.response, 'bot');
            } else if (data.error) {
                addMessage("Sorry, I encountered an error: " + data.error, 'bot');
            }
        })
        .catch(error => {
            removeMessage(loadingId);
            addMessage("Sorry, connection error.", 'bot');
            console.error('Error:', error);
        });
    });

    function addMessage(text, sender, isLoading = false) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', sender);
        if (isLoading) messageDiv.id = 'loading-msg';
        
        const contentDiv = document.createElement('div');
        contentDiv.classList.add('message-content');
        contentDiv.textContent = text;
        
        messageDiv.appendChild(contentDiv);
        chatMessages.appendChild(messageDiv);
        
        // Scroll to bottom
        chatMessages.scrollTop = chatMessages.scrollHeight;

        return messageDiv.id; // Return ID if needed
    }

    function removeMessage(id) {
        const msg = document.getElementById(id);
        if (msg) msg.remove();
    }
});
