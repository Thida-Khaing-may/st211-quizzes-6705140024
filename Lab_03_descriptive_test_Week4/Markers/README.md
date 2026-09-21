# Lab_03 Pytest Markers

- **Course:** 192-211 Automated Software Testing
- **Student:** Thida Khaing 6705140024
- **Student ID** 6705140024
- **Lab:** 03 — Custom Markers in Pytest


## What this folder covers

This folder demonstrates how to use **pytest markers** to group tests by purpose.

The tests use three custom markers:

* `smoke` — tests important functions that should work
* `slow` — tests that may take more time to run
* `regression` — tests that check previously fixed problems

The markers are registered in `pytest.ini` so pytest can recognize them.

## Files

```text
Markers/
├── pytest.ini
├── README.md
└── test_markers.py
```

* **`pytest.ini`** — registers the custom pytest markers.
* **`test_markers.py`** — contains example tests using the markers.
* **`README.md`** — explains the purpose and usage of this folder.

## Markers used

| Marker       | Purpose                                 | Example              |
| ------------ | --------------------------------------- | -------------------- |
| `smoke`      | Checks critical parts of the system     | Login, checkout      |
| `slow`       | Identifies tests that may take longer   | Report generation    |
| `regression` | Checks that an old bug has not returned | Previously fixed bug |

## Running the tests

Run all tests:

```bash
pytest
```

Run only smoke tests:

```bash
pytest -m smoke
```

Run only slow tests:

```bash
pytest -m slow
```

Run only regression tests:

```bash
pytest -m regression
```

Markers can also be combined. For example:

```bash
pytest -m "smoke or regression"
```

## Example

The test file contains tests such as:

```python
@pytest.mark.smoke
def test_critical_login():
    assert True
```

The `@pytest.mark.smoke` line labels the test as a smoke test. This allows pytest to run it separately from tests with other markers.

## Result

The tests are currently simple examples using `assert True`. The main purpose of this folder is to practice **organizing and selecting tests with pytest markers**, rather than testing a real application.
