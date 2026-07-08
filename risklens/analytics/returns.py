import pandas as pd


def compute_simple_returns(prices: pd.DataFrame) -> pd.DataFrame:
    """Compute simple close-to-close returns for each symbol."""
    ordered = prices.sort_values(["symbol", "date"]).copy()
    ordered["return"] = ordered.groupby("symbol")["close"].pct_change()
    return ordered.dropna(subset=["return"]).reset_index(drop=True)
