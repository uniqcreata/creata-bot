from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

OLLAMA_API = "http://localhost:11434/api/generate"
MODEL = "llama3"  # change if you downloaded another model

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]

    # Send request to Ollama
    response = requests.post(OLLAMA_API, json={
        "model": MODEL,
        "prompt": user_input
    }, stream=True)

    bot_reply = ""
    for line in response.iter_lines():
        if line:
            try:
                data = line.decode("utf-8")
                if '"response":"' in data:
                    text = data.split('"response":"')[1].split('"')[0]
                    bot_reply += text
            except:
                pass

    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
