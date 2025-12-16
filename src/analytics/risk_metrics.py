import pandas as pd
import numpy as np


def calculate_var(returns: pd.Series, confidence_level: float = 0.95) -> float:
    """
    Calculate Value at Risk (VaR) using historical method.
    """
    returns = returns.dropna()
    if returns.empty:
        return np.nan

    return np.percentile(returns, (1 - confidence_level) * 100)


def calculate_max_drawdown(prices: pd.Series) -> float:
    """
    Calculate maximum drawdown.
    """
    rolling_max = prices.cummax()
    drawdown = (prices - rolling_max) / rolling_max
    return drawdown.min()


def calculate_sharpe_ratio(returns: pd.Series, risk_free_rate: float = 0.06) -> float:
    """
    Calculate annualized Sharpe Ratio.
    """
    returns = returns.dropna()
    if returns.std() == 0:
        return np.nan

    excess_returns = returns.mean() * 252 - risk_free_rate
    annualized_volatility = returns.std() * np.sqrt(252)

    return excess_returns / annualized_volatility


def add_risk_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add risk metrics to dataframe.
    """
    df = df.copy()

    df["VaR_95"] = calculate_var(df["Returns"])
    df["Max_Drawdown"] = calculate_max_drawdown(df["Close"])
    df["Sharpe_Ratio"] = calculate_sharpe_ratio(df["Returns"])

    # Simple composite risk score (0–100)
    df["Risk_Score"] = (
        abs(df["VaR_95"]) * 40 +
        abs(df["Max_Drawdown"]) * 40 +
        (1 / (df["Sharpe_Ratio"].abs() + 1)) * 20
    )

    return df
