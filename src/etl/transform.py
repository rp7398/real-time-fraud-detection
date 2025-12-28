import pandas as pd
from sklearn.preprocessing import StandardScaler
import os

RAW_DIR = "data/raw"
PROCESSED_DIR = "data/processed"
os.makedirs(PROCESSED_DIR, exist_ok=True)

TARGET_COL = "is_fraud"

# Columns that should NOT be used for ML
DROP_COLS = [
    "trans_num",
    "first",
    "last",
    "street",
    "city",
    "state",
    "job",
    "dob",
    "trans_date_trans_time"
]

def preprocess(df, scaler=None):
    df = df.copy()

    # Drop unwanted columns ONLY if they exist
    for col in DROP_COLS:
        if col in df.columns:
            df.drop(col, axis=1, inplace=True)

    # Encode categorical columns safely
    for col in df.select_dtypes(include=["object"]).columns:
        if col != TARGET_COL:
            df[col] = df[col].astype("category").cat.codes

    X = df.drop(TARGET_COL, axis=1)
    y = df[TARGET_COL]

    if scaler is None:
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
    else:
        X_scaled = scaler.transform(X)

    processed = pd.DataFrame(X_scaled, columns=X.columns)
    processed[TARGET_COL] = y.values

    return processed, scaler

def run_etl():
    train_df = pd.read_csv(f"{RAW_DIR}/train.csv")
    test_df = pd.read_csv(f"{RAW_DIR}/test.csv")

    train_processed, scaler = preprocess(train_df)
    test_processed, _ = preprocess(test_df, scaler)

    train_processed.to_csv(f"{PROCESSED_DIR}/train_processed.csv", index=False)
    test_processed.to_csv(f"{PROCESSED_DIR}/test_processed.csv", index=False)

    print("ETL completed successfully for fraudTrain dataset")

if __name__ == "__main__":
    run_etl()
