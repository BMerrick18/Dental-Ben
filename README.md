# Dental-Ben

Python project scaffold.

## Project structure

```
Dental-Ben/
├── src/
│   └── dental_ben/       # Application package
│       ├── __init__.py
│       └── main.py       # Entry point
├── tests/                # Test suite
├── pyproject.toml        # Project config & dependencies
└── README.md
```

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
pip install -e ".[dev]"
```

## Run

```bash
python -m dental_ben.main
# or after install:
dental-ben
```

## Test

```bash
pytest
```
