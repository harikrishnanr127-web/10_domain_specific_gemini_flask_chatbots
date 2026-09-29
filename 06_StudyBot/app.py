import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

app = Flask(__name__)
MODEL = "gemini-3.1-flash-lite"

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY is missing. Add it to the .env file.")

client = genai.Client(api_key=API_KEY)

with open("chatbot_config.txt", "r", encoding="utf-8") as f:
    SYSTEM_PROMPT = f.read()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    message = (data.get("message") or "").strip()

    if not message:
        return jsonify({"error": "Please enter a message."}), 400

    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=message,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                thinking_config=types.ThinkingConfig(thinking_level="minimal"),
            ),
        )
        return jsonify({"reply": response.text or "I couldn't generate a response."})
    except Exception as e:
        return jsonify({"error": f"Gemini API error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")), debug=True)
