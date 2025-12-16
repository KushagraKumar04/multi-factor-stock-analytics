# Global configuration for the project

# Default stock symbols (NSE)
DEFAULT_STOCKS = [
    "RELIANCE.NS",
    "TCS.NS",
    "INFY.NS",
    "HDFCBANK.NS"
]

# Date range for historical data
START_DATE = "2018-01-01"

# Data directories
RAW_DATA_PATH = "data/raw"
PROCESSED_DATA_PATH = "data/processed"

# Technical indicator parameters
RSI_PERIOD = 14
MACD_FAST = 12
MACD_SLOW = 26
MACD_SIGNAL = 9
BOLLINGER_WINDOW = 20
BOLLINGER_STD = 2
