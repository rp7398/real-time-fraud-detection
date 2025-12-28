import pandas as pd
import os
import subprocess
import zipfile

RAW_DIR = "data/raw"
os.makedirs(RAW_DIR, exist_ok=True)

DATASET = "mlg-ulb/creditcardfraud"
ZIP_PATH = os.path.join(RAW_DIR, "creditcardfraud.zip")
CSV_PATH = os.path.join(RAW_DIR, "creditcard.csv")


def download_dataset():
    print("Downloading dataset from Kaggle...")

    subprocess.run(
        ["kaggle", "datasets", "download", "-d", DATASET, "-p", RAW_DIR],
        check=True
    )

    with zipfile.ZipFile(ZIP_PATH, "r") as zip_ref:
        zip_ref.extractall(RAW_DIR)

    print("Dataset downloaded and extracted")


def ingest_data():
    # Download only if CSV not present (CI-safe)
    if not os.path.exists(CSV_PATH):
        download_dataset()

    df = pd.read_csv(CSV_PATH)

    # For consistency with your pipeline
    df.to_csv(f"{RAW_DIR}/train.csv", index=False)
    df.to_csv(f"{RAW_DIR}/test.csv", index=False)

    print("Train & Test data ingested successfully")


if __name__ == "__main__":
    ingest_data()
