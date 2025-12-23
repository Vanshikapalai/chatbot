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
        elif "python" in msg:
    reply = "Python is a high-level programming language widely used for AI, web development, and data science."

elif "flask" in msg:
    reply = "Flask is a lightweight Python web framework used to build web applications and APIs."

elif "chatbot" in msg:
    reply = "A chatbot is a software application that simulates human conversation using predefined logic or AI models."

elif "cloud" in msg:
    reply = "Cloud computing allows applications to run on remote servers instead of local machines."

elif "deployment" in msg:
    reply = "Deployment is the process of making an application live so users can access it online."

elif "render" in msg:
    reply = "Render is a cloud platform used to deploy and host web applications."

elif "technology" in msg:
    reply = "Technology refers to the application of scientific knowledge to solve real-world problems."

elif "future" in msg:
    reply = "The future of AI includes automation, smart systems, and intelligent decision-making tools."


    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run()
