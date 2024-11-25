$(document).ready(function () {
    console.log(Intl.DateTimeFormat().resolvedOptions().timeZone)
    
    // Initialize WebSocket connection
    var ws_url = "";
    const ws_path = '/ws/anonChat/';

    if(window.location.protocol === 'https:'){
        ws_url = 'wss://' + window.location.host + ws_path;
    }else{
        ws_url = 'ws://' + window.location.host + ws_path;
    }

    console.log({'websocket_url': ws_url});

    const socket = new WebSocket(ws_url);

    // Select elements
    const $messageInput = $('#anon-message');
    const $sendButton = $('#send-anon-message');
    const $messagesContainer = $('#messages');

    // Event: Connection opened
    socket.onopen = function () {
        console.log('WebSocket connection established.');
    };

    // Event: Message received from the server
    socket.onmessage = function (event) {
        console.log('Message received:', event.data);
    
        // Parse the JSON data
        const data = JSON.parse(event.data);
    
        // Extract the message and display it
        if (data.message) {
            /*<tr>
                <td>{{message.time}}</td>
                <td>{{message.text}}</td>
            </tr>*/
            var time_formated = data.time;
            time_formated.replace(' pm', 'p.m.').replace(' am', 'a.m.');

            const $message = $('<tr>').append($('<td>').text(time_formated)).append($('<td>').text(data.message));

            $messagesContainer.append($message);
        } else {
            console.warn('Invalid message format received:', data);
        }
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
            socket.send(JSON.stringify({ message: message })); // Send the message to the server
            console.log('Message sent:', message);

            var time = new Date();
            const monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
            const timeWithoutSeconds = time.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', hour12: false });  // `hour12: false` forces 24-hour format

            // Format as "Nov. 25, 2024, 14:55"
            var time_output = `${monthNames[time.getMonth()]} ${time.getDate()}, ${time.getFullYear()}, ${timeWithoutSeconds}`;


            const $sentMessage = $('<tr>').append($('<td>').text(time_output)).append($('<td>').text(message));
            
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
