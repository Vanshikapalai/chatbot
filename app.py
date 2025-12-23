from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    msg = data.get("message", "").lower()

    if "ai" in msg:
        reply = "Artificial Intelligence is the ability of machines to simulate human intelligence such as learning and problem solving."
    elif "machine learning" in msg:
        reply = "Machine learning is a subset of AI that allows systems to learn automatically from data."
    elif "project" in msg:
        reply = "This project demonstrates an intelligent chatbot built using Flask and modern web technologies."
    elif "hello" in msg or "hi" in msg:
        reply = "Hello! How can I help you today?"
    elif "name" in msg:
        reply = "I am an AI-based chatbot designed for academic demonstration."
    else:
        reply = "That is an interesting question. I am designed to provide intelligent responses."

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run()
