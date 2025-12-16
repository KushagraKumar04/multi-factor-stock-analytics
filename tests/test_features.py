import pandas as pd
from src.features.technical_indicators import add_technical_indicators
from src.features.statistical_features import add_statistical_features


def test_feature_generation():
    data = {
        "Close": [100, 102, 101, 103, 105, 104, 106, 108, 110, 109]
    }

    df = pd.DataFrame(data)

    df = add_technical_indicators(df)
    df = add_statistical_features(df)

    assert "RSI" in df.columns
    assert "MACD" in df.columns
    assert "Volatility_20" in df.columns
