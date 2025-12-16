import yfinance as yf
import pandas as pd
from datetime import datetime
import os

DATA_PATH = "data/raw/stocks"


def fetch_stock_data(
    symbol: str,
    start: str = "2018-01-01",
    end: str = None,
    interval: str = "1d"
) -> pd.DataFrame:
    """
    Fetch historical stock data for NSE stocks using yfinance.

    Args:
        symbol (str): Stock symbol (e.g., RELIANCE.NS)
        start (str): Start date (YYYY-MM-DD)
        end (str): End date (YYYY-MM-DD)
        interval (str): Data interval (1d, 1h, etc.)

    Returns:
        pd.DataFrame: Stock OHLCV data
    """

    if end is None:
        end = datetime.today().strftime("%Y-%m-%d")

    ticker = yf.Ticker(symbol)
    df = ticker.history(start=start, end=end, interval=interval)

    if df.empty:
        raise ValueError(f"No data returned for symbol {symbol}")

    df.reset_index(inplace=True)
    df["Symbol"] = symbol

    return df


def save_raw_data(df: pd.DataFrame, symbol: str):
    """
    Save raw stock data to data/raw folder.
    """

    os.makedirs(DATA_PATH, exist_ok=True)

    filename = f"{symbol.replace('.', '_')}_raw.csv"
    filepath = os.path.join(DATA_PATH, filename)

    df.to_csv(filepath, index=False)
    print(f"Saved raw data: {filepath}")


if __name__ == "__main__":
    # Example run
    symbol = "RELIANCE.NS"
    df = fetch_stock_data(symbol)
    save_raw_data(df, symbol)
