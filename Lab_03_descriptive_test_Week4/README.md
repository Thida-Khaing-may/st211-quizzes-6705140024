# Lab 03 — Descriptive Testing: Week 4

## Course Information

| Item | Information |
| :--- | :--- |
| **Course** | 192-211 Automated Software Testing |
| **Student** | Thida Khaing |
| **Student ID** | 6705140024 |
| **Lab** | Week 4 — Descriptive Testing |

---

## 1. Overview

This Week 4 laboratory focuses on fundamental and intermediate automated software testing techniques using Python and `pytest`. Automated testing ensures software components behave predictably under both normal and exceptional operational conditions.

The lab is organized into three distinct exercises, each exploring a specific facet of test engineering:
- **Advanced Assertions & Data Structure Testing:** Verifying floating-point numbers with precision tolerances, sequence equality, order-independent list contents, dictionary mappings, and mathematical set operations.
- **Test Organization & Test Classes:** Grouping related tests inside pytest test classes (`Test*`) to maintain logical boundaries, test independence, and clean failure diagnostics.
- **Positive and Negative Validation Testing:** Balancing happy-path verification with defensive exception testing using `pytest.raises()`, boundary value analysis, and strict type and range constraints.

Each exercise contains its own dedicated test suite and comprehensive documentation.

---

## 2. Project Structure

Below is the actual directory and file layout of this laboratory:

```text
Lab_03_descriptive_test_Week4/
├── README.md                                  # Root laboratory overview and navigation
├── ShoppingCart/                              # Exercise 1: Organized tests with test classes
│   ├── shopping.py                            # ShoppingCart class implementation
│   ├── test_shopping.py                       # Unit tests grouped in TestShoppingCart class
│   └── README.md                              # Detailed ShoppingCart documentation
├── Assertion_Testing/                         # Exercise 2: Assertion techniques across data types
│   ├── test_floats.py                         # Floating-point precision and approx() tests
│   ├── test_collections.py                    # Assertions on lists, dicts, and sets
│   └── README.md                              # Detailed Assertion Testing documentation
└── Positive and Negative Testing/             # Exercise 3: Validation and exception handling
    ├── validators.py                          # Email regex and age validation logic
    ├── test_positive.py                       # Positive (happy-path) test suite
    ├── test_negative.py                       # Negative (exception-handling) test suite
    └── README.md                              # Detailed Positive & Negative Testing documentation
```

---

## 3. Exercise Overview

| Folder | Main Topic | Important Concepts | Main Python Files |
| :--- | :--- | :--- | :--- |
| **`ShoppingCart`** | Organized Unit Testing | Test classes (`TestShoppingCart`), test organization, AAA pattern, test independence, pytest discovery conventions (`Test*`, `test_*`, no `__init__`) | `shopping.py`<br>`test_shopping.py` |
| **`Assertion_Testing`** | Data-Type-Specific Assertions | Native `assert`, `pytest.approx`, IEEE 754 float precision, list equality & ordering, list normalization via `sorted()`, dictionary key-value mapping equality, set intersection (`&`), set union (`\|`) | `test_floats.py`<br>`test_collections.py` |
| **`Positive and Negative Testing`** | Input Validation & Error Handling | Happy-path acceptance, defensive rejection, `pytest.raises()`, boundary value analysis ($0$ and $150$), two-tier validation, `TypeError` (wrong type) vs. `ValueError` (invalid format/range) | `validators.py`<br>`test_positive.py`<br>`test_negative.py` |

---

## 4. Navigation to Each Exercise

### ShoppingCart
Demonstrates how to model an e-commerce shopping cart and organize test cases inside a structured test class while maintaining full test independence.
- [Read the ShoppingCart documentation](ShoppingCart/README.md)

### Assertion Testing
Explores how different Python data types—including floating-point approximations, lists, dictionaries, and sets—require tailored assertion operators and normalization strategies.
- [Read the Assertion Testing documentation](Assertion_Testing/README.md)

### Positive and Negative Testing
Demonstrates defensive test design by verifying that well-formed inputs return successful boolean values while malformed formats, out-of-range values, and illegal types raise specific, expected exceptions.
- [Read the Positive and Negative Testing documentation](<Positive and Negative Testing/README.md>)

---

## 5. How to Run the Tests

All tests are executed using `pytest`. From the command terminal, navigate to the root laboratory directory:

```bash
cd Lab_03_descriptive_test_Week4
```

### 1. Run all tests in the entire lab
```bash
pytest -v
```
This command instructs pytest to recursively discover and execute all test files across all three subdirectories.

### 2. Run ShoppingCart tests
```bash
pytest ShoppingCart -v
# or target the specific file:
pytest ShoppingCart/test_shopping.py -v
```

### 3. Run Assertion Testing tests
```bash
pytest Assertion_Testing -v
```

### 4. Run Positive and Negative Testing tests
```bash
pytest "Positive and Negative Testing" -v
```

### What the `-v` Flag Means
The `-v` (verbose) flag expands pytest's standard condensed output (`.`) into a descriptive listing showing the test file, class name, test method name, and individual pass/fail status.

---

## 6. Testing Concepts Learned

### Assertions
Assertions form the automated verification backbone of unit testing. Using Python's native `assert actual == expected`, tests programmatically confirm that a function or expression produces the intended output without requiring manual inspection.

### Test Organization
Structuring tests into classes (e.g., `class TestShoppingCart:`) groups related test cases together, isolates domain models, cleans up test reporting, and enables class-level fixtures and markers.

### Positive Testing
Positive testing verifies the "happy path"—ensuring that valid, well-formed data is properly accepted by the application and produces expected outcomes.

### Negative Testing
Negative testing ensures that corrupt, ill-formed, or invalid inputs are safely intercepted and rejected by the application before causing system crashes or undefined states.

### Exception Testing
Using pytest's `with pytest.raises(ExpectedException):` context manager allows tests to assert that an operation raises the exact expected exception class, distinguishing between data type errors (`TypeError`) and data format/range errors (`ValueError`).

### Boundary Testing
Testing edge cases at the boundaries of valid intervals (such as age values `0` and `150`) exposes off-by-one errors and boundary condition defects where software bugs frequently hide.

### Floating-Point Testing
Because computers represent decimal fractions in binary floating-point (IEEE 754), arithmetic like `0.1 + 0.2` results in minute rounding discrepancies (`0.30000000000000004`). Utilizing `pytest.approx()` enables robust equality comparisons within safe numerical tolerances.

---

## 7. Expected / Actual Test Results

The laboratory repository defines **31 total test functions** across its three exercise folders:
- **`ShoppingCart/test_shopping.py`**: 4 test methods in `TestShoppingCart`
- **`Assertion_Testing/test_floats.py`**: 2 test functions
- **`Assertion_Testing/test_collections.py`**: 5 test functions
- **`Positive and Negative Testing/test_positive.py`**: 6 test functions
- **`Positive and Negative Testing/test_negative.py`**: 14 test functions

> Test results should be recorded after running `pytest -v` from the repository root.

When executed in an environment with Python and `pytest` installed, each test runs in isolation, evaluates its assertions against the defined specifications, and confirms expected behavior.

---

## 8. Learning Outcomes

Completing this laboratory provided practical, hands-on experience in:

1. **Automated Test Design:** Constructing unit tests systematically from functional requirements and validation rules rather than writing ad-hoc test scripts.
2. **Pytest Discovery Conventions:** Correctly adhering to file (`test_*.py`), class (`Test*`), and method (`test_*`) naming rules for automated discovery.
3. **Data-Specific Assertion Strategies:** Applying appropriate comparisons based on data semantics (using `approx` for floats, `sorted()` for order-independent lists, key-value comparisons for dictionaries, and set operators).
4. **Defensive Testing & Exception Contracts:** Writing tests that verify not only that bad input fails, but that it fails with the exact intended exception type (`TypeError` vs. `ValueError`).
5. **Boundary Condition Analysis:** Validating extreme allowed input limits ($0$ and $150$) alongside nominal values.
6. **Test Independence & Suite Maintainability:** Designing self-contained test functions with no shared mutable state, ensuring tests run deterministically in any order.
