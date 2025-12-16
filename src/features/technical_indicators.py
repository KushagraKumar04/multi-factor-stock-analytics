import pandas as pd
import numpy as np
from src.utils.config import (
    RSI_PERIOD,
    MACD_FAST,
    MACD_SLOW,
    MACD_SIGNAL,
    BOLLINGER_WINDOW,
    BOLLINGER_STD,
)


def calculate_rsi(df: pd.DataFrame) -> pd.Series:
    delta = df["Close"].diff()
    gain = np.where(delta > 0, delta, 0)
    loss = np.where(delta < 0, -delta, 0)

    avg_gain = pd.Series(gain).rolling(RSI_PERIOD).mean()
    avg_loss = pd.Series(loss).rolling(RSI_PERIOD).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    return rsi


def calculate_macd(df: pd.DataFrame):
    ema_fast = df["Close"].ewm(span=MACD_FAST, adjust=False).mean()
    ema_slow = df["Close"].ewm(span=MACD_SLOW, adjust=False).mean()

    macd = ema_fast - ema_slow
    signal = macd.ewm(span=MACD_SIGNAL, adjust=False).mean()

    return macd, signal


def calculate_bollinger_bands(df: pd.DataFrame):
    sma = df["Close"].rolling(BOLLINGER_WINDOW).mean()
    std = df["Close"].rolling(BOLLINGER_WINDOW).std()

    upper_band = sma + (BOLLINGER_STD * std)
    lower_band = sma - (BOLLINGER_STD * std)

    return upper_band, lower_band


def add_technical_indicators(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["RSI"] = calculate_rsi(df)

    df["MACD"], df["MACD_Signal"] = calculate_macd(df)

    df["BB_Upper"], df["BB_Lower"] = calculate_bollinger_bands(df)

    return df
