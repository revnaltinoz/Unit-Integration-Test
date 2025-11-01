
# Python Testing Demo (Option A: Basic Functions)

A super-simple repository to demonstrate **unit tests**, **integration tests**, and **GitHub Actions CI** in class.

## What's inside?
- `app/math_utils.py` — tiny functions: `add`, `multiply`
- `app/operations.py` — uses both to compute `(a + b) * c`
- `tests/test_unit.py` — unit tests for single functions (incl. edge cases)
- `tests/test_integration.py` — integration test across modules
- `.github/workflows/tests.yml` — CI that runs tests automatically

## Run locally
```bash
# (Optional) create a virtual environment
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate

pip install -r requirements.txt
pytest -q
```

## Explain in class (script)
1) **Unit test** = tests one function (fast, isolated): open `tests/test_unit.py`.

2) **Integration test** = tests modules together: open `tests/test_integration.py`.

3) Run `pytest -q` locally → all tests green.

4) Push to GitHub → Actions tab shows CI green check ✅ on each push/PR.

## Repo structure
```
python-testing-demo-basic/
├─ app/
│  ├─ math_utils.py
│  └─ operations.py
├─ tests/
│  ├─ test_unit.py
│  └─ test_integration.py
├─ .github/workflows/tests.yml
├─ requirements.txt
└─ README.md
```
# Unit-Integration-Test
