import argparse
from pathlib import Path

from risklens.analytics.returns import compute_simple_returns
from risklens.data.loaders import load_price_csv


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Load prices and compute simple returns.")
    parser.add_argument("csv_path", type=Path, help="Path to a long-form CSV with date,symbol,close")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    prices = load_price_csv(args.csv_path)
    returns = compute_simple_returns(prices)
    symbols = ", ".join(sorted(prices["symbol"].unique()))
    print(f"Loaded {len(prices)} price rows for {symbols}")
    print(f"Computed {len(returns)} return rows")
    print(returns.tail().to_string(index=False))


if __name__ == "__main__":
    main()
