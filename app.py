from flask import Flask, jsonify
import os
import requests

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return jsonify({"message": "🚀 Creata-Bot is live with Bybit!"})

# Ping route for Render health check
@app.route("/ping")
def ping():
    return jsonify({"status": "ok", "message": "pong"})

# Signal route (basic version)
@app.route("/signal")
def signal():
    try:
        # Example: Fetch BTCUSDT price from Bybit
        response = requests.get(
            "https://api.bybit.com/v2/public/tickers?symbol=BTCUSDT"
        )
        data = response.json()

        if "result" in data and len(data["result"]) > 0:
            price = float(data["result"][0]["last_price"])

            # Simple strategy example: decide buy/sell/hold
            if price < 60000:
                action = "BUY"
            elif price > 70000:
                action = "SELL"
            else:
                action = "HOLD"

            return jsonify({
                "symbol": "BTCUSDT",
                "price": price,
                "signal": action
            })

        return jsonify({"error": "No data from Bybit"}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
