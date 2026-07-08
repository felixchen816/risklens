from pathlib import Path

import pandas as pd
import pytest

from risklens.data.loaders import load_price_csv
from risklens.data.validators import validate_price_frame


SAMPLE_PATH = Path("sample_data/prices_sample.csv")


def test_load_price_csv_reads_and_sorts_sample_data() -> None:
    prices = load_price_csv(SAMPLE_PATH)

    assert list(prices.columns) == ["date", "symbol", "close"]
    assert len(prices) == 8
    assert prices["symbol"].unique().tolist() == ["QQQ", "SPY"]


def test_validator_rejects_duplicate_symbol_date_rows() -> None:
    prices = pd.DataFrame(
        {
            "date": pd.to_datetime(["2026-01-02", "2026-01-02"]),
            "symbol": ["SPY", "SPY"],
            "close": [100.0, 101.0],
        }
    )

    with pytest.raises(ValueError, match="duplicate"):
        validate_price_frame(prices)


def test_validator_rejects_nonpositive_close_prices() -> None:
    prices = pd.DataFrame(
        {
            "date": pd.to_datetime(["2026-01-02"]),
            "symbol": ["SPY"],
            "close": [0.0],
        }
    )

    with pytest.raises(ValueError, match="nonpositive"):
        validate_price_frame(prices)
