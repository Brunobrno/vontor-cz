$(document).ready(function () {
    // Initialize WebSocket connection
    const socket = new WebSocket('ws://your-websocket-server-url');

    // Select elements
    const $messageInput = $('#anon-message');
    const $sendButton = $('#send-anon-message');
    const $messagesContainer = $('.messages');

    // Event: Connection opened
    socket.onopen = function () {
        console.log('WebSocket connection established.');
    };

    // Event: Message received from the server
    socket.onmessage = function (event) {
        console.log('Message received:', event.data);

        // Append the received message to the messages container
        const $message = $('<p>').text(event.data);
        $messagesContainer.append($message);
    };

    // Event: Connection closed
    socket.onclose = function () {
        console.warn('WebSocket connection closed.');
    };

    // Event: Error occurred
    socket.onerror = function (error) {
        console.error('WebSocket error:', error);
    };

    // Send message to the server when the button is clicked
    $sendButton.on('click', function () {
        const message = $messageInput.val().trim();

        if (message && socket.readyState === WebSocket.OPEN) {
            socket.send(message); // Send the message to the server
            console.log('Message sent:', message);

            // Optionally, display the message in the UI as "sent by user"
            const $sentMessage = $('<p>').text(`You: ${message}`).css('font-style', 'italic');
            $messagesContainer.append($sentMessage);

            // Clear the input field
            $messageInput.val('');
        } else {
            console.warn('Cannot send message. WebSocket is not open or message is empty.');
        }
    });

    // Allow pressing Enter to send the message
    $messageInput.on('keypress', function (event) {
        if (event.key === 'Enter') {
            $sendButton.click(); // Trigger the click event on the button
        }
    });
});
