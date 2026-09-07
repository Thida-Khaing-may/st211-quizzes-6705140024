# Lab 2: Writing Effective Test Cases

Automated Software Testing (192-211)  
International College, Siam University

## Overview

This lab demonstrates what separates a valuable, maintainable unit test from a fragile one using Python and `pytest`. It focuses on three core principles:
1. **The AAA Pattern (Arrange, Act, Assert)**: Structuring test cases cleanly into setup, execution, and verification steps.
2. **Test Independence**: Avoiding shared mutable state across test functions so tests can run in isolation and in any order.
3. **Boundary Value Analysis (BVA)**: Designing tests for exact boundaries, edge cases, and invalid inputs where software defects commonly hide.

## Project Structure

```text
Lab_02_effective_test_cases/
├── bank.py               # BankAccount implementation (deposit, withdraw, input validation)
├── test_bank.py          # Bank tests exploring the AAA pattern
├── test_dependent.py     # Example of shared global state (order-dependent tests)
├── test_independent.py   # Independent tests where each test owns its fresh instance
├── grades.py             # Score-to-letter-grade mapping with boundary conditions
├── test_grade.py         # Boundary value test suite for letter grades
└── README.md             # Documentation, concepts, and run instructions
```

## Key Concepts Demonstrated

### 1. The AAA Pattern (Arrange-Act-Assert)
- **Arrange**: Set up the test environment and input data (e.g., `account = BankAccount(100)`).
- **Act**: Execute the single behavior under test (e.g., `account.deposit(50)`).
- **Assert**: Verify the resulting state or return value matches expectations (e.g., `assert account.balance == 150`).

### 2. Test Independence vs. Shared State
- **Problem (`test_dependent.py`)**: Tests share a global `shared_account = BankAccount(100)` instance. `test_b_withdraw` assumes `test_a_deposit` ran first; running `test_b_withdraw` alone causes false failure.
- **Solution (`test_independent.py`)**: Each test creates its own fresh `BankAccount(100)` instance. Tests can now run standalone or in any order without interference.

### 3. Boundary Value Analysis (`grades.py` & `test_grade.py`)
Tests are placed at the exact boundary values where off-by-one errors typically occur:
- **Threshold Boundaries**:
  - Score `80` (boundary for grade `'A'`) vs. `79` (just below, grade `'B'`)
  - Score `60` (boundary for grade `'C'`) vs. `59` (just below, grade `'F'`)
- **Extreme Limits**:
  - Minimum valid score: `0` (`'F'`)
  - Maximum valid score: `100` (`'A'`)
  - Below minimum (invalid): `-1` (raises `ValueError`)

## Prerequisites

- Python 3.10+
- `pytest`

Install pytest if needed:
```bash
pip install pytest
```

## Running the Tests

Navigate to the `Lab_02_effective_test_cases` directory:

```bash
cd Lab_02_effective_test_cases
```

### Run All Tests
```bash
python -m pytest -v
```

### Run Independent Bank Tests
```bash
python -m pytest test_independent.py -v
```

### Run Grade Boundary Tests
```bash
python -m pytest test_grade.py -v
```

### Sample Output

```text
============================= test session starts =============================
platform win32 -- Python 3.14.2, pytest-9.1.1, pluggy-1.6.0
collected 11 items

test_bank.py ..                                                          [ 18%]
test_dependent.py ..                                                     [ 36%]
test_grade.py .....                                                      [ 81%]
test_independent.py ..                                                   [100%]

============================= 11 passed in 0.18s ==============================
```
