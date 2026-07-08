import pandas as pd


def validate_price_frame(prices: pd.DataFrame) -> None:
    """Raise ValueError when price data is unsafe for basic return calculations."""
    required = {"date", "symbol", "close"}
    missing = sorted(required - set(prices.columns))
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(missing)}")

    if prices.empty:
        raise ValueError("Price data is empty")

    if prices[["date", "symbol", "close"]].isna().any().any():
        raise ValueError("Price data contains missing dates, symbols, or close prices")

    duplicates = prices.duplicated(["date", "symbol"])
    if duplicates.any():
        raise ValueError("Price data contains duplicate date/symbol rows")

    if (prices["close"] <= 0).any():
        raise ValueError("Price data contains nonpositive close prices")
