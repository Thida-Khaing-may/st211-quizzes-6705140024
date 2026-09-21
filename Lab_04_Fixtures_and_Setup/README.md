# Lab 04 — Fixtures and Test Setup

## Course Information

| Item            | Information                        |
| :-------------- | :--------------------------------- |
| **Course**      | 192-211 Automated Software Testing |
| **Student**     | Thida Khaing                       |
| **Student ID**  | 6705140024                         |
| **Lab**         | Lab 04 — Fixtures and Test Setup   |
| **Institution** | Siam University                    |

---

## 1. Overview

This laboratory focuses on **test fixtures and test setup** using Python and `pytest`.

The first topic covered in this lab is **pytest Fixtures**. Fixtures are used to provide reusable test data or objects to test functions and help reduce repeated setup code.

The current exercise uses a simple `BankAccount` class to demonstrate how a fixture can create an account with a predefined starting balance.

Additional topics and exercises can be added to this laboratory as they are introduced during the course.

---

## 2. Project Structure

```text
Lab_04_Fixtures_and_Set_Up/
│
├── README.md
│
└── Fixtures/
    ├── README.md
    ├── bank.py
    └── test_bank.py
```

### Current Topics

| Topic                            | Status      |
| :------------------------------- | :---------- |
| **Pytest Fixtures**              | Completed   |
| **Reusable Test Setup**          | Practiced   |
| **Fixture-based Test Functions** | Practiced   |
| **Additional Lab 04 Topics**     | To be added |

---

## 3. Current Exercise — Fixtures

The current exercise demonstrates how to use a pytest fixture to create a reusable `BankAccount` object.

The fixture provides an account with an initial balance of `100`.

```python
@pytest.fixture
def account():
    return BankAccount(100)
```

The fixture is then used by multiple tests:

```python
def test_deposit(account):
    account.deposit(50)
    assert account.balance == 150


def test_withdraw(account):
    account.withdraw(30)
    assert account.balance == 70
```

This allows both tests to use the same setup without creating the `BankAccount` object separately inside each test.

---

## 4. What I Practiced

In today's exercise, I practiced:

* Creating a pytest fixture using `@pytest.fixture`
* Providing test data or objects through a fixture
* Passing a fixture into a test function
* Reusing the same fixture in multiple tests
* Reducing repeated test setup code
* Using fixtures to provide a consistent starting condition for tests

---

## 5. Test Setup

The fixture creates:

```text
BankAccount(100)
```

The two tests then perform different operations.

```text
Fixture
   │
   ▼
BankAccount(100)
   │
   ├── test_deposit
   │      └── 100 + 50 = 150
   │
   └── test_withdraw
          └── 100 - 30 = 70
```

Each test receives the fixture as the `account` parameter.

---

## 6. Running the Current Tests

Run the tests from the `Lab_04_Fixtures_and_Set_Up` directory.

```bash
pytest -v
```

Or run only the current Fixtures exercise:

```bash
pytest Fixtures/test_bank.py -v
```

The current exercise contains two tests:

```text
test_deposit
test_withdraw
```

Expected result:

```text
2 passed
```

---

## 7. Learning Progress

### Completed

* [x] Pytest Fixtures
* [x] Reusable Test Setup
* [x] Using Fixtures as Test Parameters

### To Be Added

Future topics and exercises will be added to this Lab 04 directory as they are covered in class.

---

## 8. Learning Outcome

After today's exercise, I understand that a pytest fixture can be used to prepare reusable test data or objects before a test runs.

Instead of repeating:

```python
account = BankAccount(100)
```

inside every test, the fixture provides the account automatically:

```python
def test_deposit(account):
```

This makes the test code shorter and keeps the test setup separate from the behavior being tested.
