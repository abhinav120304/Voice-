function sendMessage() {
    var userInput = document.getElementById("user-input").value;
    if (userInput.trim() === "") return;
    
    addToChat("You: " + userInput);
    document.getElementById("user-input").value = "";
    
    processCommand(userInput);
}

function addToChat(message) {
    var chatBox = document.getElementById("chat-box");
    chatBox.innerHTML += "<p>" + message + "</p>";
    chatBox.scrollTop = chatBox.scrollHeight;
}

function processCommand(command) {
    // Placeholder function for processing commands.
    // Here you can handle the commands and send responses back to the chat.
    // Example:
    // if (command.toLowerCase() === "hello") {
    //     addToChat("Assistant: Hi there!");
    // }
}
