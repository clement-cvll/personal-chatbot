// Make sure we wait that the user message is treated and the response is received
// before we enable the input.

// Send the user message to the server
function sendMessage() {
    // Get the elements from the page
    var userInput = document.getElementById("user-input");
    var submitButton = document.querySelector("button");

    // Disable the form elements during processing
    userInput.disabled = true;
    submitButton.disabled = true;

    // Get the message from the text box
    var userMessage = userInput.value;

    // Send AJAX request to the server
    fetch("/add_input", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: 'user_message=' + encodeURIComponent(userMessage),
    })
    .then(response => {
        // Re-enable the form elements
        userInput.disabled = false;
        submitButton.disabled = false;

        // Refresh the conversation
        location.reload();
    })
    .catch(error => console.error(error));  
}
