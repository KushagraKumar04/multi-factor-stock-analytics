import pandas as pd
import numpy as np
from sklearn.cluster import KMeans


def prepare_regime_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Prepare features used for market regime detection.
    """
    features = df[["Returns", "Volatility_20"]].dropna()
    return features


def detect_market_regime(df: pd.DataFrame, n_regimes: int = 3) -> pd.DataFrame:
    """
    Detect market regimes using clustering.

    Regimes:
    0/1/2 → later mapped to Bull / Bear / Sideways
    """

    df = df.copy()

    features = prepare_regime_features(df)

    kmeans = KMeans(n_clusters=n_regimes, random_state=42)
    regimes = kmeans.fit_predict(features)

    features["Regime"] = regimes

    # Merge regime labels back to main dataframe
    df = df.merge(
        features[["Regime"]],
        left_index=True,
        right_index=True,
        how="left"
    )

    return df


def label_regimes(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert numeric regimes into meaningful labels.
    """
    df = df.copy()

    regime_stats = (
        df.groupby("Regime")[["Returns", "Volatility_20"]]
        .mean()
        .sort_values(by=["Returns", "Volatility_20"])
    )

    regime_mapping = {}
    labels = ["Bear", "Sideways", "Bull"]

    for regime, label in zip(regime_stats.index, labels):
        regime_mapping[regime] = label

    df["Market_Regime"] = df["Regime"].map(regime_mapping)

    return df
