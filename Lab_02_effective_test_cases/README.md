# Lab 02 — Writing Effective Test Cases

## Course Information

| Item           | Information                                 |
| :------------- | :------------------------------------------ |
| **Course**     | 192-211 Automated Software Testing          |
| **Student**    | Thida Khaing                                |
| **Student ID** | 6705140024                                  |
| **Lab**        | Week 3 — Effective Test Cases & Test Design |

---

## 1. Overview

The purpose of this laboratory is to practice writing **effective and reliable test cases** using Python and `pytest`.

A good test case should have the following qualities:

* **Focused** — tests one clear behavior or condition.
* **Independent** — does not depend on another test running first.
* **Repeatable** — produces the same result whenever it is executed under the same conditions.
* **Readable** — has a clear test name and simple test structure.
* **Fast** — executes quickly so that tests can be run frequently during development.

In this lab, I applied these principles to two simple Python programs:

1. A `BankAccount` class for testing deposits and withdrawals.
2. A `letter_grade()` function for testing grade boundaries and invalid input.

The lab also demonstrates why poorly designed tests can produce misleading results, especially when tests share mutable state.

---

## 2. Project Structure

The project contains the following files:

```text
Lab_02_effective_test_cases/
│
├── README.md
├── bank.py
├── test_bank.py
├── test_bad_example.py
├── test_dependent.py
├── test_independent.py
├── grades.py
└── test_grade.py
```

### File Description

| File                  | Purpose                                                                                                                         |
| :-------------------- | :------------------------------------------------------------------------------------------------------------------------------ |
| `bank.py`             | Contains the `BankAccount` class with deposit and withdrawal operations.                                                        |
| `test_bank.py`        | Contains basic tests for the `BankAccount` class, including a simple deposit test and a test that performs multiple operations. |
| `test_bad_example.py` | Demonstrates a test design where several operations are tested together instead of focusing on one behavior.                    |
| `test_dependent.py`   | Demonstrates the problem of shared mutable state between tests.                                                                 |
| `test_independent.py` | Demonstrates independent tests where each test creates its own `BankAccount` object.                                            |
| `grades.py`           | Contains the `letter_grade()` function that converts a score into a letter grade.                                               |
| `test_grade.py`       | Tests valid boundaries, grade thresholds, and invalid scores using Boundary Value Analysis.                                     |

---

# 3. Core Concepts & Exercise Breakdown

## 3.1 AAA Pattern — Arrange, Act, Assert

The **AAA pattern** is a simple structure for organizing test cases.

| Stage       | Meaning                                                      | Example in This Lab              |
| :---------- | :----------------------------------------------------------- | :------------------------------- |
| **Arrange** | Prepare the objects and data needed for the test.            | Create `BankAccount(100)`.       |
| **Act**     | Perform the operation being tested.                          | Call `account.deposit(50)`.      |
| **Assert**  | Check whether the actual result matches the expected result. | Check that the balance is `150`. |

### Example

```python
def test_deposit_increases_balance():

    # Arrange
    account = BankAccount(100)

    # Act
    new_balance = account.deposit(50)

    # Assert
    assert new_balance == 150
```

### My Testing Logic

First, I create a bank account with an initial balance of `100`. This is the **Arrange** step.

Next, I deposit `50`. This is the **Act** step because it is the behavior I want to test.

Finally, I check whether the returned balance is `150`. This is the **Assert** step.

This makes the purpose of the test easy to understand.

---

## 3.2 AAA vs. Testing Everything at Once

A test can technically perform several operations and still pass, but this does not always make it a good test.

For example:

```python
def test_everything_at_once():

    account = BankAccount(100)

    account.deposit(50)
    account.withdraw(30)
    account.deposit(10)

    assert account.balance == 130
```

This test performs three different operations:

1. Deposit `50`
2. Withdraw `30`
3. Deposit `10`

The final assertion only checks the final balance.

### Comparison

| Focused AAA Test           | Everything-at-Once Test                             |
| :------------------------- | :-------------------------------------------------- |
| Tests one behavior clearly | Tests several operations together                   |
| Easier to understand       | More difficult to identify the failing operation    |
| Easier to debug            | Debugging requires checking several operations      |
| More focused               | Less focused                                        |
| Easier to maintain         | Can become complicated as more operations are added |

### What I Learned

The purpose is not that multiple operations are always incorrect. Instead, **focused tests make failures easier to understand**.

If the focused deposit test fails, I know that the problem is related to the deposit behavior.

If the `test_everything_at_once` test fails, I have to investigate several operations before knowing which part caused the problem.

---

# 3.3 Test Independence vs. Shared Mutable State

Test independence means that one test should not depend on another test being executed first.

The following example demonstrates a problem with **shared mutable state**:

```python
shared_account = BankAccount(100)

def test_a_deposit():

    shared_account.deposit(50)

    assert shared_account.balance == 150

def test_b_withdraw():

    shared_account.withdraw(30)

    assert shared_account.balance == 120
```

Both tests use the same `shared_account` object.

### What Happens?

Initially:

```text
shared_account.balance = 100
```

When `test_a_deposit()` runs:

```text
100 + 50 = 150
```

The balance becomes:

```text
150
```

Then `test_b_withdraw()` runs:

```text
150 - 30 = 120
```

Therefore, when both tests are run together, the second test can pass.

However, if I run `test_b_withdraw()` alone, the account starts at:

```text
100
```

After withdrawing `30`:

```text
100 - 30 = 70
```

Therefore, an assertion expecting `120` fails.

### Why Is This a Problem?

The result of `test_b_withdraw()` depends on the previous execution of `test_a_deposit()`.

This violates test independence.

The test should be able to run:

* by itself,
* in a different order,
* repeatedly,
* or together with other tests,

without changing its expected result.

---

# 3.4 Independent Test Setup

To solve the shared-state problem, each test creates its own `BankAccount` object.

```python
def test_deposit_independent():

    account = BankAccount(100)

    account.deposit(50)

    assert account.balance == 150


def test_withdraw_independent():

    account = BankAccount(100)

    account.withdraw(30)

    assert account.balance == 70
```

### Why This Is Better

Each test starts with a fresh account:

```text
test_deposit_independent
100 → 150
```

and:

```text
test_withdraw_independent
100 → 70
```

The tests do not share the same mutable object.

Therefore, the result of one test cannot change the starting state of another test.

### Main Lesson

> Each test should prepare its own required state instead of depending on state created by another test.

This makes the tests more reliable, repeatable, and easier to debug.

---

# 3.5 Boundary Value Analysis (BVA)

The `letter_grade()` function accepts scores from `0` to `100`.

The grading rules are:

| Score Range | Grade   |
| :---------- | :------ |
| `80–100`    | A       |
| `70–79`     | B       |
| `60–69`     | C       |
| `0–59`      | F       |
| Below `0`   | Invalid |
| Above `100` | Invalid |

Boundary Value Analysis focuses on values around important limits because errors often occur at boundaries.

### Important Boundary Values

| Boundary            | Value to Test | Expected Result |
| :------------------ | :-----------: | :-------------- |
| Minimum valid value |      `0`      | F               |
| Below minimum       |      `-1`     | `ValueError`    |
| A boundary          |      `80`     | A               |
| Just below A        |      `79`     | B               |
| B boundary          |      `70`     | B               |
| Just below B        |      `69`     | C               |
| C boundary          |      `60`     | C               |
| Just below C        |      `59`     | F               |
| Maximum valid value |     `100`     | A               |
| Above maximum       |     `101`     | `ValueError`    |

### Test Examples

```python
def test_boundary_a_grade():

    assert letter_grade(80) == "A"
    assert letter_grade(79) == "B"
```

This test checks the boundary between **A and B**.

```python
def test_boundary_pass_fail():

    assert letter_grade(60) == "C"
    assert letter_grade(59) == "F"
```

This test checks the boundary between **C and F**.

```python
def test_minimum_valid():

    assert letter_grade(0) == "F"
```

This verifies the minimum valid score.

```python
def test_maximum_valid():

    assert letter_grade(100) == "A"
```

This verifies the maximum valid score.

```python
def test_below_minimum_invalid():

    with pytest.raises(ValueError):
        letter_grade(-1)
```

This checks that an invalid negative score raises the expected exception.

### My Testing Logic

I did not test only normal values such as `50`, `75`, and `90`.

Instead, I selected values around the important boundaries:

```text
80 → A
79 → B

70 → B
69 → C

60 → C
59 → F
```

This helps verify that the program changes grades at exactly the correct threshold.

I also tested the minimum and maximum valid values and an invalid value below the minimum.

---

# 4. How to Run the Tests

All commands should be executed from the `Lab_02_effective_test_cases` directory.

## 4.1 Run All Tests

```bash
pytest -v
```

The `-v` option means **verbose**.

It displays the name and result of each individual test instead of showing only a short summary.

---

## 4.2 Run the Bank Account Tests

```bash
pytest test_bank.py -v
```

This runs the tests related to the `BankAccount` class.

---

## 4.3 Run the Grade Tests

```bash
pytest test_grade.py -v
```

This runs the Boundary Value Analysis tests for `letter_grade()`.

---

## 4.4 Run the Independent Tests

```bash
pytest test_independent.py -v
```

These tests demonstrate that each test creates its own account and does not depend on shared state.

---

## 4.5 Run the Dependent Tests

```bash
pytest test_dependent.py -v
```

This demonstrates the shared mutable state problem.

Depending on the execution order and the test implementation, the tests may pass together because one test changes the shared account before another test uses it.

---

## 4.6 Run the Withdrawal Test Alone

To demonstrate why the shared-state design is problematic, the withdrawal test can be executed independently.

For example:

```bash
pytest test_dependent.py::test_b_withdraw -v
```

When the test is run alone, `shared_account` starts with a balance of `100`.

After withdrawing `30`:

```text
100 - 30 = 70
```

However, the test expects:

```text
120
```

Therefore, the test fails.

This demonstrates that the test incorrectly depends on the state created by `test_a_deposit()`.

---

# 5. Testing Concepts Learned

### AAA Pattern

I learned to organize tests into:

```text
Arrange → Act → Assert
```

This makes the purpose and logic of each test clearer.

### Test Independence

I learned that tests should not depend on another test running first. Creating a fresh object inside each test prevents shared mutable state from affecting results.

### Boundary Value Analysis

I learned to test values at and around important boundaries, such as:

```text
80 / 79
70 / 69
60 / 59
0 / -1
100 / 101
```

### Descriptive Test Naming

Names such as:

```text
test_deposit_increases_balance
test_boundary_a_grade
test_minimum_valid
test_below_minimum_invalid
```

describe what the test is checking.

A descriptive name makes it easier to understand a failure without immediately reading the test code.

---

# 6. Expected Test Execution Summary

After implementing the tests correctly, the test suite should report passing tests for the independent bank-account tests and grade boundary tests.

A representative successful run may look like:

```text
============================= test session starts =============================

collected 10 items

test_bank.py::test_deposit_increases_balance PASSED
test_bank.py::test_everything_at_once PASSED
test_independent.py::test_deposit_independent PASSED
test_independent.py::test_withdraw_independent PASSED
test_grade.py::test_boundary_a_grade PASSED
test_grade.py::test_boundary_pass_fail PASSED
test_grade.py::test_minimum_valid PASSED
test_grade.py::test_maximum_valid PASSED
test_grade.py::test_below_minimum_invalid PASSED

============================== 9 passed in ...s ===============================
```

> **Note:** The exact number of collected tests depends on the final contents of each test file. The important result is that the intended independent and boundary tests pass, while the deliberately dependent example can be demonstrated separately to show the shared-state problem.

---

# 7. Learning Outcomes

After completing this laboratory, I can:

1. **Apply the AAA pattern** to organize tests into Arrange, Act, and Assert sections.
2. **Identify test independence problems** caused by shared mutable state.
3. **Create isolated test setups** so that each test can run independently.
4. **Apply Boundary Value Analysis** to test values at, above, and below important limits.
5. **Write descriptive test names** that clearly communicate the behavior being tested.
6. **Use pytest commands and verbose output** to execute, inspect, and debug individual test cases.

Overall, this laboratory helped me understand that effective testing is not only about making assertions pass. A well-designed test should also be **focused, independent, repeatable, readable, and fast**. These qualities make a test suite easier to maintain and more useful for finding defects.
