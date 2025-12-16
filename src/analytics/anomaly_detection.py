import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest


def detect_zscore_anomalies(
    series: pd.Series,
    window: int = 20,
    threshold: float = 3.0
) -> pd.Series:
    """
    Detect anomalies using rolling Z-score.
    """
    rolling_mean = series.rolling(window).mean()
    rolling_std = series.rolling(window).std()

    z_score = (series - rolling_mean) / rolling_std
    anomalies = abs(z_score) > threshold

    return anomalies


def detect_isolation_forest_anomalies(
    df: pd.DataFrame,
    features: list,
    contamination: float = 0.03
) -> pd.Series:
    """
    Detect anomalies using Isolation Forest.
    """
    data = df[features].dropna()

    if data.empty:
        return pd.Series(index=df.index, data=False)

    model = IsolationForest(
        n_estimators=100,
        contamination=contamination,
        random_state=42
    )

    preds = model.fit_predict(data)

    anomaly_flags = pd.Series(index=data.index, data=(preds == -1))

    return anomaly_flags.reindex(df.index, fill_value=False)


def add_anomaly_flags(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add anomaly detection flags to dataframe.
    """
    df = df.copy()

    # Price-based anomalies
    df["Price_Anomaly"] = detect_zscore_anomalies(df["Returns"])

    # ML-based anomalies
    df["ML_Anomaly"] = detect_isolation_forest_anomalies(
        df,
        features=["Returns", "Volatility_20"]
    )

    # Combined anomaly signal
    df["Anomaly_Flag"] = df["Price_Anomaly"] | df["ML_Anomaly"]

    return df
