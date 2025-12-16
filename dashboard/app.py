import streamlit as st
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath("."))


from src.ingestion.stock_api import fetch_stock_data
from src.features.technical_indicators import add_technical_indicators
from src.features.statistical_features import add_statistical_features
from src.analytics.regime_detection import detect_market_regime, label_regimes
from src.analytics.risk_metrics import add_risk_metrics
from src.analytics.anomaly_detection import add_anomaly_flags
from src.utils.config import DEFAULT_STOCKS, START_DATE


st.set_page_config(
    page_title="Stock Market Intelligence Platform",
    layout="wide"
)

st.title("📊 Multi-Factor Stock Market Intelligence Platform")
st.caption("Enterprise-grade analytics for NSE stocks")

# ---------------- SIDEBAR ---------------- #
st.sidebar.header("⚙️ Configuration")

symbol = st.sidebar.selectbox(
    "Select NSE Stock",
    DEFAULT_STOCKS
)

# ---------------- DATA PIPELINE ---------------- #
@st.cache_data
def load_data(symbol):
    df = fetch_stock_data(symbol, start=START_DATE)
    df = add_technical_indicators(df)
    df = add_statistical_features(df)
    df = detect_market_regime(df)
    df = label_regimes(df)
    df = add_risk_metrics(df)
    df = add_anomaly_flags(df)
    return df


df = load_data(symbol)

# ---------------- KPI ROW ---------------- #
latest = df.iloc[-1]

col1, col2, col3, col4 = st.columns(4)

col1.metric("Last Price", f"₹ {latest['Close']:.2f}")
col2.metric("Market Regime", latest["Market_Regime"])
col3.metric("Sharpe Ratio", f"{latest['Sharpe_Ratio']:.2f}")
col4.metric("Risk Score", f"{latest['Risk_Score']:.1f}")

# ---------------- PRICE CHART ---------------- #
st.subheader("📈 Price Trend")

st.line_chart(
    df.set_index("Date")[["Close"]],
    height=350
)

# ---------------- TECHNICAL INDICATORS ---------------- #
st.subheader("📐 Technical Indicators")

col1, col2 = st.columns(2)

with col1:
    st.line_chart(
        df.set_index("Date")[["RSI"]],
        height=250
    )

with col2:
    st.line_chart(
        df.set_index("Date")[["MACD", "MACD_Signal"]],
        height=250
    )

# ---------------- REGIME DISTRIBUTION ---------------- #
st.subheader("🌐 Market Regime Distribution")

st.bar_chart(
    df["Market_Regime"].value_counts()
)

# ---------------- ANOMALY ALERTS ---------------- #
st.subheader("🚨 Anomaly Detection")

anomalies = df[df["Anomaly_Flag"]]

if anomalies.empty:
    st.success("No anomalies detected recently.")
else:
    st.warning(f"{len(anomalies)} anomalous events detected.")
    st.dataframe(
        anomalies[["Date", "Close", "Anomaly_Flag"]].tail(10),
        width="stretch"
    )

# ---------------- RISK SECTION ---------------- #
st.subheader("⚠️ Risk Metrics Summary")

risk_df = df[[
    "VaR_95",
    "Max_Drawdown",
    "Sharpe_Ratio",
    "Risk_Score"
]].tail(1)

st.dataframe(risk_df, width="stretch")

# ---------------- FOOTER ---------------- #
st.caption(
    "Built using Python, Streamlit, and advanced market analytics | For Data Analyst roles"
)
