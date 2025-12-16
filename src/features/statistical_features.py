import pandas as pd
import numpy as np


def add_statistical_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Daily returns
    df["Returns"] = df["Close"].pct_change()

    # Rolling volatility
    df["Volatility_20"] = df["Returns"].rolling(20).std()

    # Drawdown
    rolling_max = df["Close"].cummax()
    df["Drawdown"] = (df["Close"] - rolling_max) / rolling_max

    # Z-score of returns
    df["ZScore_Returns"] = (
        (df["Returns"] - df["Returns"].rolling(20).mean())
        / df["Returns"].rolling(20).std()
    )

    return df
