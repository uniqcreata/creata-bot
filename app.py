from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

# ✅ Load API keys from Render environment
BYBIT_API_KEY = os.getenv("BYBIT_API_KEY")
BYBIT_API_SECRET = os.getenv("BYBIT_API_SECRET")
ALPHA_VANTAGE_KEY = os.getenv("ALPHA_VANTAGE_KEY")  # for forex

@app.route("/")
def home():
    return "🚀 Creata-Bot is Live! Ask me for crypto & forex signals."

# ==============================
# 🔹 Price Endpoint
# ==============================
@app.route("/price", methods=["GET"])
def get_price():
    pair = request.args.get("pair", "BTCUSDT")

    # If it's forex like EURUSD, use Alpha Vantage
    if len(pair) == 6 and pair.isalpha():
        url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={pair[:3]}&to_currency={pair[3:]}&apikey={ALPHA_VANTAGE_KEY}"
        r = requests.get(url).json()
        try:
            price = r["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
            return jsonify({"pair": pair, "price": price})
        except:
            return jsonify({"error": "Forex data not available"}), 400

    # Otherwise treat it as crypto from Bybit
    url = f"https://api.bybit.com/v5/market/tickers?category=spot&symbol={pair}"
    r = requests.get(url).json()
    try:
        price = r["result"]["list"][0]["lastPrice"]
        return jsonify({"pair": pair, "price": price})
    except:
        return jsonify({"error": "Crypto data not available"}), 400

# ==============================
# Run
# ==============================
if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)
@app.route("/ping")
def ping():
    return {"status": "ok", "message": "Creata-Bot is alive 🚀"}
