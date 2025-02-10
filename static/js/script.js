function correctText() {
    let text = document.getElementById("userInput").value;

    fetch('/correct', {
        method: "POST",
        body: JSON.stringify({ text: text }),
        headers: { "Content-Type": "application/json" }
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("correctedOutput").innerText = "✅ Corrected: " + data.corrected_text;
    })
    .catch(error => console.error("Error:", error));
}
