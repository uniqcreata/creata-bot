from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 Creata-Bot is live!"

@app.route("/trade-advice")
def trade_advice():
    # For now, just return simple JSON advice (later we’ll connect real forex/crypto APIs)
    return jsonify({
        "market": "BTC/USDT",
        "advice": "Consider buying if price drops near 26,500, take profit around 27,200",
        "note": "This is dummy advice – real logic coming soon."
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
