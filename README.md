# RiskLens

RiskLens is a Python toolkit for portfolio risk analytics. It starts with local CSV price data, validates common data problems, computes simple returns, and will grow into reproducible portfolio risk reports.

## Current Features

- Load long-form daily price data from CSV.
- Validate required columns, missing values, duplicate date/symbol rows, and nonpositive prices.
- Compute simple close-to-close returns by symbol.
- Run a small command-line demo on bundled sample data.
- Test the loader, validator, and returns logic.

## Quickstart

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
pytest
```

Try the sample loader:

```bash
python -m risklens.cli sample_data/prices_sample.csv
```

## Repository Layout

```text
risklens/
  data/
    loaders.py
    validators.py
  analytics/
    returns.py
  cli.py
sample_data/
tests/
```

## Data Format

Input CSV files should use long-form price data:

```csv
date,symbol,close
2026-01-02,SPY,100.00
2026-01-05,SPY,101.00
```

## Limitations

This is not financial advice and not a prediction engine. The first version uses tiny sample data only so the code and tests stay easy to understand.

## Roadmap

- Add annualized volatility, Sharpe ratio, max drawdown, VaR, and CVaR.
- Compare equal-weight, inverse-volatility, and minimum-variance allocations.
- Export Markdown risk reports.
- Add charts and a small reproducible demo report.
