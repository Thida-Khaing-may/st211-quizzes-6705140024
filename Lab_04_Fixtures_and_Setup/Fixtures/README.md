# Lab_04: Fixtures — BankAccount Test Setup

## Course Information

| Item            | Information                        |
| :-------------- | :--------------------------------- |
| **Course**      | 192-211 Automated Software Testing |
| **Student**     | Thida Khaing                       |
| **Student ID**  | 6705140024                         |
| **Lab**         | Lab 04 — Fixtures and Test Setup   |
| **Topic**       | Pytest Fixtures                    |
| **Institution** | Siam University                    |

---

## 1. Overview

This exercise introduces **pytest Fixtures**.

A fixture is a reusable setup function that provides data or objects needed by test functions.

In this exercise, the fixture creates a `BankAccount` object with an initial balance of `100`.

The same fixture is used by two tests:

* `test_deposit`
* `test_withdraw`

This demonstrates how fixtures can reduce repeated setup code and provide a consistent starting state for tests.

---

## 2. Project Structure

```text
Fixtures/
│
├── README.md
├── bank.py
└── test_bank.py
```

### File Description

| File           | Purpose                                                           |
| :------------- | :---------------------------------------------------------------- |
| `README.md`    | Explains the fixture exercise and testing approach.               |
| `bank.py`      | Contains the `BankAccount` class.                                 |
| `test_bank.py` | Contains the pytest fixture and tests for deposit and withdrawal. |

---

# 3. BankAccount Class

The `BankAccount` class is defined in `bank.py`.

```python
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        return self.balance
```

The class contains:

* A `balance` attribute
* A `deposit()` method
* A `withdraw()` method

---

## 3.1 Initial Balance

The constructor is:

```python
def __init__(self, balance=0):
    self.balance = balance
```

If no balance is provided, the default is `0`.

For this exercise, the fixture creates the account with:

```python
BankAccount(100)
```

Therefore, the starting balance for each test is:

```text
100
```

---

## 3.2 Deposit Method

The `deposit()` method adds money to the account.

```python
account.deposit(50)
```

Starting with `100`:

```text
100 + 50 = 150
```

The method also checks that the deposit amount is positive.

```python
if amount <= 0:
    raise ValueError("Deposit amount must be positive.")
```

---

## 3.3 Withdraw Method

The `withdraw()` method subtracts money from the account.

```python
account.withdraw(30)
```

Starting with `100`:

```text
100 - 30 = 70
```

The method checks whether the requested withdrawal is greater than the available balance.

```python
if amount > self.balance:
    raise ValueError("Insufficient funds.")
```

---

# 4. Pytest Fixture

The main concept in this exercise is the pytest fixture.

The fixture is defined in `test_bank.py`:

```python
@pytest.fixture
def account():
    return BankAccount(100)
```

The `@pytest.fixture` decorator tells pytest that `account()` is a fixture.

The fixture prepares the test object:

```text
BankAccount(100)
```

and makes it available to tests that request the `account` fixture.

---

# 5. Using the Fixture in Tests

A fixture can be passed into a test function by using the fixture name as a parameter.

For example:

```python
def test_deposit(account):
```

Here, `account` is not created directly inside the test.

Pytest automatically provides the object returned by the fixture.

The process is:

```text
@pytest.fixture
     │
     ▼
account()
     │
     ▼
BankAccount(100)
     │
     ▼
test_deposit(account)
```

---

# 6. Deposit Test

The first test is:

```python
def test_deposit(account):
    account.deposit(50)
    assert account.balance == 150
```

### Test Flow

The fixture provides:

```text
Initial balance = 100
```

The test performs:

```text
deposit(50)
```

The resulting balance is:

```text
100 + 50 = 150
```

The assertion checks:

```python
assert account.balance == 150
```

Expected result:

```text
PASSED
```

---

# 7. Withdraw Test

The second test is:

```python
def test_withdraw(account):
    account.withdraw(30)
    assert account.balance == 70
```

### Test Flow

The fixture provides:

```text
Initial balance = 100
```

The test performs:

```text
withdraw(30)
```

The resulting balance is:

```text
100 - 30 = 70
```

The assertion checks:

```python
assert account.balance == 70
```

Expected result:

```text
PASSED
```

---

# 8. Why Use a Fixture?

Without a fixture, the setup would have to be repeated:

```python
def test_deposit():
    account = BankAccount(100)
    account.deposit(50)
    assert account.balance == 150


def test_withdraw():
    account = BankAccount(100)
    account.withdraw(30)
    assert account.balance == 70
```

Both tests contain:

```python
account = BankAccount(100)
```

With a fixture, the setup is written once:

```python
@pytest.fixture
def account():
    return BankAccount(100)
```

The tests can then focus on the behavior being tested:

```python
def test_deposit(account):
    account.deposit(50)
    assert account.balance == 150


def test_withdraw(account):
    account.withdraw(30)
    assert account.balance == 70
```

This reduces duplication and makes the test setup easier to maintain.

---

# 9. Fixture and Test Isolation

The fixture is also useful for giving each test a consistent starting condition.

The deposit test changes its account from:

```text
100 → 150
```

The withdrawal test starts with its own fixture-created account:

```text
100 → 70
```

Conceptually:

```text
test_deposit
    │
    └── BankAccount(100)
            │
            └── deposit(50)
                    │
                    └── 150


test_withdraw
    │
    └── BankAccount(100)
            │
            └── withdraw(30)
                    │
                    └── 70
```

The tests do not need to rely on the result of another test.

---

# 10. Important Syntax

The fixture decorator should be written exactly as:

```python
@pytest.fixture
```

Python is case-sensitive.

Therefore:

```python
@pytest.Fixture
```

is incorrect.

The correct test file begins with:

```python
import pytest
from bank import BankAccount


@pytest.fixture
def account():
    return BankAccount(100)
```

Then the tests can use the fixture:

```python
def test_deposit(account):
    account.deposit(50)
    assert account.balance == 150


def test_withdraw(account):
    account.withdraw(30)
    assert account.balance == 70
```

---

# 11. Running the Tests

Run the following command from the `Lab_04_Fixtures_and_Set_Up` directory:

```bash
pytest Fixtures/test_bank.py -v
```

Or, if you are already inside the `Fixtures` directory:

```bash
pytest -v
```

The expected result is:

```text
test_bank.py::test_deposit PASSED
test_bank.py::test_withdraw PASSED

2 passed
```

---

# 12. Key Concepts Learned

### Pytest Fixture

A fixture provides reusable test setup:

```python
@pytest.fixture
def account():
    return BankAccount(100)
```

### Fixture Parameter

The fixture can be requested by adding its name to the test function:

```python
def test_deposit(account):
```

### Reusable Setup

The same fixture can be used by multiple tests without repeating the setup code.

### Test Isolation

Each test can start from the same defined initial condition.

### Separation of Setup and Test Behavior

The fixture handles preparation, while the test focuses on the behavior being checked.

---

# 13. Learning Outcome

After completing this exercise, I can:

1. Create a pytest fixture using `@pytest.fixture`.
2. Provide a reusable object through a fixture.
3. Use a fixture as a test function parameter.
4. Reduce repeated setup code.
5. Give tests a consistent starting condition.
6. Run fixture-based tests using pytest.

---

# 14. Conclusion

This exercise introduced pytest Fixtures through a simple `BankAccount` example.

The `account` fixture creates a `BankAccount` with an initial balance of `100`. Both the deposit and withdrawal tests use this fixture instead of creating the account themselves.

The main idea learned from this exercise is that **fixtures separate reusable test setup from the actual test behavior**.

```text
Fixture
   ↓
BankAccount(100)
   ↓
┌─────────────────┬──────────────────┐
│ test_deposit    │ test_withdraw    │
│ 100 + 50 = 150  │ 100 - 30 = 70    │
└─────────────────┴──────────────────┘
```

This provides a simple and reusable way to prepare test conditions in pytest.
