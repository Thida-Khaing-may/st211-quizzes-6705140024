# Roman Numeral Converter

A Python program that converts Roman numerals into integers with strict validation according to standard Roman numeral rules.

## Description

The Roman Numeral Converter provides functionality to:
- Convert standard Roman numeral strings (e.g., `XIV`, `MCMXCIV`) into their corresponding integer values.
- Validate Roman numerals to ensure they follow proper Roman numeral grammar (e.g., valid subtractive notation like `IV`, `IX`, `XL`, `XC`, `CD`, `CM`, and disallow invalid combinations like `IIII`, `VV`, `VX`, `XXC`).
- Provide an interactive command-line interface (CLI) for users to convert numbers.

## Folder Structure

```text
RomanNumeral/
├── source/
│   ├── __init__.py
│   └── roman.py          # Core conversion logic and interactive CLI
├── tests/
│   └── test_roman.py     # Unit tests using pytest
└── README.md             # Documentation and usage instructions
```

## Prerequisites

- Python 3.10+
- `pytest` (for running tests)

Install pytest if not already installed:
```bash
pip install pytest
```

## How to Run the Application

Navigate to the `RomanNumeral` directory and run:

```bash
python source/roman.py
```

### Sample CLI Run

```text
--- Roman Numeral Converter ---
1. Convert Roman Numeral
2. Exit
Choose an option: 1
Enter a Roman Numeral: XIV
XIV = 14

--- Roman Numeral Converter ---
1. Convert Roman Numeral
2. Exit
Choose an option: 1
Enter a Roman Numeral: MCMXCIV
MCMXCIV = 1994

--- Roman Numeral Converter ---
1. Convert Roman Numeral
2. Exit
Choose an option: 2
Thank you for using the Roman Numeral Converter! See you next time.
```

## How to Run the Tests

From the `RomanNumeral` directory, run pytest:

```bash
python -m pytest tests/
```

Or from the repository root:
```bash
python -m pytest RomanNumeral/tests/
```

### Sample Test Output

```text
============================= test session starts =============================
platform win32 -- Python 3.14.2, pytest-9.1.1, pluggy-1.6.0
rootdir: RomanNumeral
collected 6 items

tests/test_roman.py ......                                               [100%]

============================== 6 passed in 0.09s ==============================
```

## Test Coverage

The test suite in [`tests/test_roman.py`](tests/test_roman.py) verifies:
- **Category 1 - Single Symbol**: Basic numerals like `I`, `V`.
- **Category 2 - Repeated Symbols**: Additive repeated numerals like `II`, `III`.
- **Category 3 - Different Symbols**: Combinations in descending order like `VI`, `XVI`.
- **Category 4 - Subtractive Notation**: Standard subtraction pairs like `IV`, `IX`.
- **Category 5 - Digit + Subtractive Notation**: Complex numbers like `XIX`.
- **Category 6 - Invalid Input**: Error handling for invalid syntax (`VX`, `XXC`, `IIII`, `VV`), invalid characters (`ABC`), empty strings (`""`), and non-string inputs.
