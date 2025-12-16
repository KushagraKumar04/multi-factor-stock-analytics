import yfinance as yf
import pandas as pd
from datetime import datetime
import os
import time

DATA_PATH = "data/raw/stocks"


def fetch_stock_data(
    symbol: str,
    start: str = "2018-01-01",
    end: str = None,
    interval: str = "1d",
    retries: int = 3,
    sleep_seconds: int = 2
) -> pd.DataFrame:
    """
    Fetch historical stock data for NSE stocks using yfinance
    with retry and rate-limit handling.

    Args:
        symbol (str): Stock symbol (e.g., RELIANCE.NS)
        start (str): Start date (YYYY-MM-DD)
        end (str): End date (YYYY-MM-DD)
        interval (str): Data interval (1d, 1h, etc.)
        retries (int): Number of retry attempts
        sleep_seconds (int): Wait time between retries

    Returns:
        pd.DataFrame: Stock OHLCV data
    """

    if end is None:
        end = datetime.today().strftime("%Y-%m-%d")

    last_exception = None

    for attempt in range(retries):
        try:
            ticker = yf.Ticker(symbol)
            df = ticker.history(start=start, end=end, interval=interval)

            if df.empty:
                raise ValueError(f"No data returned for symbol {symbol}")

            df.reset_index(inplace=True)
            df["Symbol"] = symbol

            return df

        except Exception as e:
            last_exception = e
            time.sleep(sleep_seconds)

    # Final failure after retries
    raise RuntimeError(
        f"Failed to fetch data for {symbol} after {retries} retries"
    ) from last_exception


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
