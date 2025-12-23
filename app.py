from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
import os

app = Flask(__name__)

# Configure Gemini safely
api_key = os.getenv("GOOGLE_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
else:
    model = None


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(force=True)
    user_message = data.get("message", "").lower()

    # TRY GEMINI
    if model:
        try:
            response = model.generate_content(user_message)
            return jsonify({"reply": response.text})
        except Exception:
            pass  # fall back silently

    # SMART FALLBACK (AI-like)
    if "ai" in user_message:
        reply = "Artificial Intelligence is the simulation of human intelligence in machines."
    elif "hello" in user_message or "hi" in user_message:
        reply = "Hello! How can I help you today?"
    elif "project" in user_message:
        reply = "This project demonstrates an AI-powered chatbot using modern web technologies."
    else:
        reply = "That’s an interesting question. Let me help you with that."

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run()
