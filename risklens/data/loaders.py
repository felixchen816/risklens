from pathlib import Path

import pandas as pd

from risklens.data.validators import validate_price_frame


REQUIRED_COLUMNS = ["date", "symbol", "close"]


def load_price_csv(path: str | Path) -> pd.DataFrame:
    """Load long-form daily price data with date, symbol, and close columns."""
    csv_path = Path(path)
    prices = pd.read_csv(csv_path, parse_dates=["date"])
    missing_columns = sorted(set(REQUIRED_COLUMNS) - set(prices.columns))
    if missing_columns:
        raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")

    prices = prices[REQUIRED_COLUMNS].copy()
    prices["symbol"] = prices["symbol"].astype(str).str.upper().str.strip()
    prices = prices.sort_values(["symbol", "date"]).reset_index(drop=True)
    validate_price_frame(prices)
    return prices
