# Clinic Stock Checker (practice challenge)

A small Python tool a vet clinic uses to track its medicine stock.
The previous developer left before finishing, and some functions have bugs.

## Setup

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m pytest -v
```

Some tests will fail. That's expected.

## tasks 

1. **Fix the bugs** in `inventory/stock.py` so the tests pass.
   Do not change the tests. They describe the correct behaviour.
2. **Implement `low_stock`**, which currently raises `NotImplementedError`.
   Its docstring and its tests describe what it should do.
3. **Write `NOTES.md`** with a few bullet points: what each bug was,
   how you found it, and anything you would improve with more time.
   You'll talk through this, as in the real interview.

## Data

`data/stock.csv` holds one row per product, with:
`name, category, quantity, expiry` (expiry is `YYYY-MM-DD`).
