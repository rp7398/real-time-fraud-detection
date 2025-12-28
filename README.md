# 🚨 Real-Time Fraud Detection System with MLOps

> **An end-to-end, production-grade fraud detection platform built using Machine Learning, Docker, and Jenkins CI/CD.**
> This project demonstrates the complete lifecycle of a real-world data science system — from raw data ingestion to automated deployment.

🌐 **Live Project Report:**  
👉 https://rp7398.github.io/report/

---

## 📌 Project Overview

Financial fraud is a critical challenge for banks and digital payment platforms.
This project implements a **Real-Time Fraud Detection System** that:

- Ingests large-scale transaction data
- Performs robust data preprocessing and feature engineering
- Trains and evaluates machine learning models
- Exposes predictions via a REST API
- Automates training and deployment using **MLOps practices**
- Ensures reproducibility using **Docker and CI/CD**

This repository represents a **full-stack Data Science + MLOps solution**, developed as part of an **MSc Data Science capstone project**.

---

## 🎯 Objectives

- Detect fraudulent transactions with high precision
- Handle highly imbalanced real-world data
- Separate experimentation (notebooks) from production code
- Deploy the trained model as a real-time API
- Automate the entire pipeline using CI/CD

---

## 🧠 Key Features

- ✔ End-to-End ML Pipeline (Ingestion → ETL → Training → Deployment)
- ✔ Real Kaggle Fraud Dataset
- ✔ Feature Engineering for Categorical & Numerical Data
- ✔ REST API for Real-Time Predictions
- ✔ Dockerized Deployment
- ✔ Jenkins-based CI/CD Pipeline
- ✔ Reproducible & Modular Codebase
- ✔ Academic + Industry Aligned Architecture

---

## 🏗️ System Architecture

Raw Data  
→ Data Ingestion  
→ ETL & Feature Engineering  
→ Exploratory Data Analysis (Jupyter)  
→ Model Training & Evaluation  
→ Model Serialization  
→ Flask REST API  
→ Docker Container  
→ Jenkins CI/CD Deployment

---

## 🛠️ Tech Stack

### Programming & ML
- Python
- Pandas, NumPy
- Scikit-learn

### Data Analysis
- Jupyter Notebook
- Matplotlib, Seaborn

### Backend & Deployment
- Flask (REST API)
- Docker

### Automation & DevOps
- Jenkins (CI/CD)
- Git & GitHub

---

## 📂 Project Structure

real-time-fraud-detection-mlops/
├── api/
├── src/
├── notebooks/
├── data/
├── models/
├── docker/
├── jenkins/
├── requirements.txt
├── README.md
└── .gitignore

---

## 📊 Dataset

- **Source:** Kaggle Credit Card Transaction Dataset
- **Files:** fraudTrain.csv, fraudTest.csv
- **Target:** is_fraud
- **Challenge:** Highly imbalanced classification problem

---

## 🌐 REST API

### Health Check
GET /health

Response:
{
  "status": "UP"
}

### Prediction
POST /predict

---

## 🐳 Docker

docker build -t fraud-detection -f docker/Dockerfile .
docker run -d -p 5000:5000 fraud-detection

---

## 🔄 CI/CD with Jenkins

The Jenkins pipeline automates:
- Data ingestion
- ETL
- Model training
- Docker image build
- API deployment

---

## 🎓 Academic Relevance

Developed as part of an **MSc Data Science Capstone Project**, showcasing real-world ML engineering and MLOps practices.

---

## 🚀 Future Enhancements

- Streaming with Kafka
- Model monitoring & drift detection
- Auto retraining
- Cloud deployment (AWS/GCP)

---

## 👤 Author

**Rajat Pathak**  
MSc Data Science
