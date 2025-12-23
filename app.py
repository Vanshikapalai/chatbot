from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    msg = data["message"].lower()

    if "hello" in msg or "hi" in msg:
        reply = "Hello! How can I help you today?"

    elif "day" in msg or "date" in msg:
        reply = "Today is a great day to build something amazing!"

    elif "python" in msg:
        reply = "Python is a popular programming language used in AI, web development, and data science."

    elif "flask" in msg:
        reply = "Flask is a lightweight Python web framework used to build web applications."

    elif "chatbot" in msg:
        reply = "A chatbot is a program that simulates human conversation using logic or AI."

    elif "ai" in msg:
        reply = "Artificial Intelligence allows machines to simulate human intelligence."

    elif "future" in msg:
        reply = "The future of AI includes automation, smart assistants, and intelligent systems."

    else:
        reply = "That’s an interesting question. I’m here to help!"

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run()
