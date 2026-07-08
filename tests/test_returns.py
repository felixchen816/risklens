import pandas as pd
import pytest

from risklens.analytics.returns import compute_simple_returns


def test_compute_simple_returns_by_symbol() -> None:
    prices = pd.DataFrame(
        {
            "date": pd.to_datetime(
                ["2026-01-02", "2026-01-03", "2026-01-02", "2026-01-03"]
            ),
            "symbol": ["SPY", "SPY", "QQQ", "QQQ"],
            "close": [100.0, 110.0, 200.0, 190.0],
        }
    )

    returns = compute_simple_returns(prices)

    assert len(returns) == 2
    spy_return = returns.loc[returns["symbol"] == "SPY", "return"].iloc[0]
    qqq_return = returns.loc[returns["symbol"] == "QQQ", "return"].iloc[0]
    assert spy_return == pytest.approx(0.10)
    assert qqq_return == pytest.approx(-0.05)
