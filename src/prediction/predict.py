import joblib
import numpy as np

MODEL_PATH = "models/fraud_model.pkl"
model = joblib.load(MODEL_PATH)

def predict_transaction(features):
    features = np.array(features).reshape(1, -1)
    probability = model.predict_proba(features)[0][1]
    return probability
