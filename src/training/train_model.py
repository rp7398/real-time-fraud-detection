import pandas as pd
import joblib
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

PROCESSED_DIR = "data/processed"
MODEL_DIR = "models"
TARGET_COL = "is_fraud"

os.makedirs(MODEL_DIR, exist_ok=True)

def train():
    train_df = pd.read_csv(f"{PROCESSED_DIR}/train_processed.csv")
    test_df = pd.read_csv(f"{PROCESSED_DIR}/test_processed.csv")

    X_train = train_df.drop(TARGET_COL, axis=1)
    y_train = train_df[TARGET_COL]

    X_test = test_df.drop(TARGET_COL, axis=1)
    y_test = test_df[TARGET_COL]

    model = RandomForestClassifier(
        n_estimators=200,
        class_weight="balanced",
        random_state=42,
        n_jobs=-1
    )

    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    print("Evaluation on Test Data:")
    print(classification_report(y_test, preds))

    joblib.dump(model, f"{MODEL_DIR}/fraud_model.pkl")
    print("Model saved successfully")

if __name__ == "__main__":
    train()
