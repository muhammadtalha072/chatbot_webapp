from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder="templates")

# Simple predefined responses
responses = {
    "hi": "Hello! How can I assist you today?",
    "how are you": "I'm an AI, but I'm always ready to help!",
    "bye": "Goodbye! Have a great day!"
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").lower()
    bot_response = responses.get(user_message, "I'm still learning! Can you rephrase?")
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
