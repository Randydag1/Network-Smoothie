// /frontend/src/main.js
const { ipcRenderer } = require("electron");
const axios = require('axios');

function submitInput() {
    // Get the user's input
    const userInput = document.getElementById("userInput").value;

    // Send the input to the backend for processing
    axios.post('http://localhost:5000/process_input', {
        input_data: userInput.split('\n') // Example: split input by new lines
    })
    .then(response => {
        // Display the result from the backend
        document.getElementById("insight").innerText = "Insight: " + response.data.insight;
    })
    .catch(error => {
        console.error("Error processing input:", error);
        document.getElementById("insight").innerText = "Error occurred. Try again.";
    });
}