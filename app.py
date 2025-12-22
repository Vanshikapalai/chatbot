from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
import os

# Flask app
app = Flask(__name__)

# Gemini config
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    user_message = data.get("message", "")

    if user_message == "":
        return jsonify({"reply": "Empty message"}), 400

    response = model.generate_content(user_message)
    return jsonify({"reply": response.text})


if __name__ == "__main__":
    app.run()
