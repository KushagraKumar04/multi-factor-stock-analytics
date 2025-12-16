# 📊 Multi-Factor Stock Market Intelligence Platform

🚀 **Live Demo**  
🔗 https://multi-factor-stock-analytics-kushagra.streamlit.app/

---

## 📌 Overview

The **Multi-Factor Stock Market Intelligence Platform** is an enterprise-grade data analytics application built to analyze **Indian stock market (NSE)** data in real time.  
Rather than focusing purely on price prediction, this project emphasizes **analytics, risk awareness, explainability, and market behavior**, which are essential skills for **Data Analyst and Analytics Engineer roles**.

The platform integrates live stock data, performs advanced feature engineering, detects market regimes, evaluates financial risk, flags anomalies, and presents insights through an **interactive Streamlit dashboard** deployed on the cloud.

---

## 🎯 Project Objectives

- Analyze live NSE stock market data
- Engineer meaningful technical and statistical features
- Detect market regimes (Bull / Bear / Sideways)
- Quantify downside risk using financial metrics
- Detect abnormal market events and anomalies
- Build a fault-tolerant, production-ready analytics system
- Deploy a public dashboard accessible to recruiters

---

## 🧠 Why This Project Is Different

Most stock market projects:
- Focus only on price prediction
- Use a single ML model
- Lack explainability and risk analysis
- Are not deployed

This project:
- Uses **multi-factor analytics instead of raw prediction**
- Includes **market regime detection**
- Focuses on **risk-adjusted insights**
- Handles **real-world API failures**
- Is **fully deployed with a live public link**

This mirrors how **real analytics teams** operate in production.

---

## 🏗️ System Architecture

```text

Live NSE Market Data (Yahoo Finance)
│
▼
Data Ingestion Layer
│
▼
Feature Engineering Engine
│
▼
Analytics Layer
(Regime Detection, Risk, Anomaly Detection)
│
▼
Explainability & Insights
│
▼
Interactive Streamlit Dashboard
│
▼
Cloud Deployment (Public URL)
```

---

## 🔑 Core Features

### 1️⃣ Live Stock Data Ingestion
- Fetches historical and near real-time NSE stock data
- Implements retry logic and rate-limit handling
- Gracefully handles API failures

---

### 2️⃣ Feature Engineering

**Technical Indicators**
- RSI (Relative Strength Index)
- MACD & Signal Line
- Bollinger Bands

**Statistical Features**
- Daily returns
- Rolling volatility
- Drawdown
- Z-score normalization

---

### 3️⃣ Market Regime Detection
- Uses unsupervised learning (K-Means clustering)
- Classifies market behavior into:
  - **Bull**
  - **Bear**
  - **Sideways**

Helps interpret market structure beyond price movement.

---

### 4️⃣ Risk & Volatility Analytics
- Value at Risk (VaR)
- Maximum Drawdown
- Sharpe Ratio (risk-adjusted return)
- Composite Risk Score

---

### 5️⃣ Anomaly & Event Detection
- Statistical anomaly detection using Z-score
- ML-based anomaly detection using Isolation Forest
- Flags abnormal price and volatility behavior

---

### 6️⃣ Explainable AI (XAI)
- SHAP-based explainability concepts
- Identifies feature importance
- Enables business-friendly interpretation of analytics

---

### 7️⃣ Interactive Dashboard
- Built using **Streamlit**
- Stock selector for NSE companies
- Live price charts and KPIs
- Technical indicators visualization
- Risk metrics and anomaly alerts

---

### 8️⃣ Fault-Tolerant Design
- Graceful fallback to demo data when live APIs are unavailable
- Dashboard never crashes
- Ensures uninterrupted user experience

---

## 🖥️ Live Dashboard

🔗 **https://multi-factor-stock-analytics-kushagra.streamlit.app/**

The dashboard allows users to:
- Select NSE stocks (RELIANCE, TCS, INFY, etc.)
- View price trends and indicators
- Analyze market regime
- Monitor risk metrics
- Detect anomalies in real time

---

## 📂 Project Structure

```text
multi-factor-stock-analytics/
│
├── dashboard/
│   └── app.py
│
├── src/
│   ├── ingestion/
│   │   └── stock_api.py
│   │
│   ├── features/
│   │   ├── technical_indicators.py
│   │   └── statistical_features.py
│   │
│   ├── analytics/
│   │   ├── regime_detection.py
│   │   ├── risk_metrics.py
│   │   └── anomaly_detection.py
│   │
│   ├── explainability/
│   │   └── shap_analysis.py
│   │
│   └── utils/
│       └── config.py
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── external/
│
├── notebooks/
├── tests/
├── requirements.txt
├── README.md
└── LICENSE

```
---

## 🛠️ Tech Stack

- **Language:** Python  
- **Data Analysis:** Pandas, NumPy  
- **Machine Learning:** Scikit-learn  
- **Finance Data:** yFinance  
- **Explainability:** SHAP  
- **Visualization & UI:** Streamlit, Plotly  
- **Deployment:** Streamlit Community Cloud  

---

## ⚙️ Run Locally

```bash
# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the dashboard
python -m streamlit run dashboard/app.py

```

## 👤 Author

Kushagra Kumar
Computer Science Engineering

🔗 Live Demo: https://multi-factor-stock-analytics-kushagra.streamlit.app/
