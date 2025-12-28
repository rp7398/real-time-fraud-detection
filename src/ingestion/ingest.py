import pandas as pd
import os

RAW_DIR = "data/raw"
os.makedirs(RAW_DIR, exist_ok=True)

def ingest_data():
    train_df = pd.read_csv("sample_data/fraudTrain.csv")
    test_df = pd.read_csv("sample_data/fraudTest.csv")

    train_df.to_csv(f"{RAW_DIR}/train.csv", index=False)
    test_df.to_csv(f"{RAW_DIR}/test.csv", index=False)

    print("Train & Test data ingested successfully")

if __name__ == "__main__":
    ingest_data()
