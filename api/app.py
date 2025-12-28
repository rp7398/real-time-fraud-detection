from flask import Flask, request, jsonify
from src.prediction.predict import predict_transaction

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "UP"}), 200


@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    features = data["features"]

    fraud_prob = predict_transaction(features)

    return jsonify({
        "fraud_probability": fraud_prob,
        "fraud": fraud_prob > 0.7
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
