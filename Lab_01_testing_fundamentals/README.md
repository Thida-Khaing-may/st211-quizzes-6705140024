# Lab 01 — Testing Fundamentals

## Course Information

| Item           | Information                                 |
| :------------- | :------------------------------------------ |
| **Course**     | 192-211 Automated Software Testing          |
| **Student**    | Thida Khaing                                |
| **Student ID** | 6705140024                                  |
| **Lab**        | Week 1 — Software Testing Motivation & Basic Testing |
---

## 1. Overview

This laboratory introduced the basic purpose of software testing and why testing is important even for small programs.

I practiced writing automated tests using Python and `pytest`. The exercises include a `NumFinder` example that demonstrates how a suitable test case can reveal a logic defect, as well as basic calculator testing exercises.

The lab covers:

* Identifying a logic problem using test cases
* Testing different input orders
* Testing edge cases
* Writing basic automated tests with `pytest`
* Using the Arrange-Act-Assert (AAA) pattern
* Testing normal results and expected exceptions
* Understanding how different test cases can reveal defects

---

## 2. Project Structure

```text
Lab_01_testing_fundamentals/
│
├── README.md
│
├── num_finder/
│   ├── num_finder.py
│   └── test_num_finder.py
│
└── Calculator_Testing/
    ├── src/
    │   └── calculator.py
    │
    └── tests/
        ├── test_first.py
        ├── test_output.py
        ├── test_calculator.py
        ├── test_exceptions.py
        └── test_failing.py
```

### File Description

| File                                          | Purpose                                                                           |
| --------------------------------------------- | --------------------------------------------------------------------------------- |
| `num_finder/num_finder.py`                    | Contains the `NumFinder` class for finding the smallest and largest values.       |
| `num_finder/test_num_finder.py`               | Tests different number orders and a single-element input.                         |
| `Calculator_Testing/src/calculator.py`        | Contains basic calculator functions: `add`, `subtract`, `multiply`, and `divide`. |
| `Calculator_Testing/tests/test_first.py`      | Contains basic `pytest` assertion exercises.                                      |
| `Calculator_Testing/tests/test_output.py`     | Demonstrates a test that prints output.                                           |
| `Calculator_Testing/tests/test_calculator.py` | Tests the calculator operations.                                                  |
| `Calculator_Testing/tests/test_exceptions.py` | Tests the expected `ValueError` when dividing by zero.                            |
| `Calculator_Testing/tests/test_failing.py`    | Contains the corrected version of the deliberate failing-test exercise.           |

---

## 3. Core Concepts & Exercise Breakdown

### 3.1 The NumFinder Example

The `NumFinder` class tracks the smallest and largest values from a list of numbers.

The original logic used an `if / elif` structure:

```python
if n < self.smallest:
    self.smallest = n
elif n > self.largest:
    self.largest = n
```

The problem is that when the first `if` condition is true, the `elif` condition is skipped.

For example, with a descending list:

```python
[4, 3, 2, 1]
```

each new value is smaller than the current smallest value. Therefore, the first condition is true and the `elif` condition is not checked.

This can cause `largest` to remain at its initial value instead of being updated correctly.

### Corrected Logic

I changed the two conditions to independent `if` statements:

```python
if n < self.smallest:
    self.smallest = n

if n > self.largest:
    self.largest = n
```

This allows every number to be checked against both the smallest and largest values.

---

### 3.2 Testing Different Input Orders

The NumFinder tests use different input orders:

| Test Input      | Expected Result            |
| --------------- | -------------------------- |
| `[4, 25, 7, 9]` | smallest = 4, largest = 25 |
| `[4, 3, 2, 1]`  | smallest = 1, largest = 4  |
| `[1, 2, 3, 4]`  | smallest = 1, largest = 4  |
| `[5]`           | smallest = 5, largest = 5  |

### Why the Descending Test Is Important

The descending-list test is useful because it can expose the original `if / elif` logic problem.

A test using only a mixed or ascending list might not reveal the defect. Testing different input orders gives better coverage of the program's behavior.

This demonstrates that one passing test does not necessarily prove that a program works correctly for all valid inputs.

---

### 3.3 Single-Element Edge Case

The single-element test uses:

```python
[5]
```

The expected result is:

```text
smallest = 5
largest = 5
```

The only value in the list must be both the smallest and largest value.

Testing this case checks that the program handles an input containing only one value correctly.

---

### 3.4 Arrange-Act-Assert (AAA) Pattern

The calculator tests also demonstrate the Arrange-Act-Assert pattern.

| Stage   | Meaning                                          | Example                          |
| ------- | ------------------------------------------------ | -------------------------------- |
| Arrange | Prepare the data or objects needed for the test. | Set the input values.            |
| Act     | Perform the operation being tested.              | Call `add(100, 250)`.            |
| Assert  | Check whether the result is correct.             | Assert that the result is `350`. |

Example:

```python
def test_add_aaa_pattern():
    # Arrange
    first_number = 100
    second_number = 250

    # Act
    result = add(first_number, second_number)

    # Assert
    assert result == 350
```

Separating these three steps makes the purpose of the test easier to understand.

---

### 3.5 Basic Pytest Assertions

The `test_first.py` file contains simple examples of `pytest` assertions.

The tests check:

* Basic arithmetic
* String conversion using `.upper()`
* The length of a list

For example:

```python
assert 1 + 1 == 2
```

This demonstrates the basic idea of a test: perform an operation and compare the actual result with the expected result.

---

### 3.6 Testing Printed Output

The `test_output.py` exercise demonstrates a test that prints a value:

```python
def test_with_print():
    value = 42
    print(f"The value is {value}")
    assert value == 42
```

The assertion checks the value, while the `print()` statement allows the value to be displayed when the test is run with pytest's `-s` option.

For example:

```bash
pytest -s
```

This exercise demonstrates that tests can contain output for observation while still using assertions to verify behavior.

---

### 3.7 Calculator Operation Testing

The `test_calculator.py` file tests the main calculator operations.

| Function     | Example           | Expected Result |
| ------------ | ----------------- | --------------: |
| `add()`      | `add(2, 3)`       |               5 |
| `subtract()` | `subtract(10, 4)` |               6 |
| `multiply()` | `multiply(3, 4)`  |              12 |
| `divide()`   | `divide(10, 2)`   |               5 |

The tests also include positive, negative, and zero values.

An explicit AAA example is included in `test_add_aaa_pattern()`.

---

### 3.8 Exception Testing

The `test_exceptions.py` file checks what happens when the program receives an invalid operation.

Division by zero should raise a `ValueError`.

The test uses `pytest.raises()`:

```python
def test_divide_by_zero_raises():
    with pytest.raises(ValueError):
        divide(10, 0)
```

Another test checks the error message:

```python
def test_divide_by_zero_message():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(5, 0)
```

This demonstrates that automated tests can check both successful results and expected errors.

---

### 3.9 Deliberate Failing Test Exercise

The `test_failing.py` exercise was used to demonstrate how an incorrect expected value causes a test to fail.

The corrected version is:

```python
def test_this_will_fail():
    result = add(2, 2)
    assert result == 4
```

The expected result was corrected from the deliberate failure so that the test now passes.

This exercise helped demonstrate the relationship between the actual result and the expected result in a test.

---

## 4. Verification of Code and Test Logic

* **`src/calculator.py`:** Arithmetic functions and zero-division handling using `ValueError` are implemented correctly.
* **`tests/test_calculator.py`:** Tests arithmetic operations using positive, negative, and zero values and includes an explicit Arrange-Act-Assert example.
* **`tests/test_exceptions.py`:** Verifies the expected `ValueError` and checks the error message using `pytest.raises(ValueError, match=...)`.
* **`tests/test_failing.py`:** Contains the corrected version of the deliberate failing-test exercise.
* **`tests/test_first.py` and `tests/test_output.py`:** Verify basic assertions, string operations, list length, and printed output.
* **`num_finder/num_finder.py`:** Uses two independent `if` statements instead of `if / elif`, resolving the descending-list update defect.
* **`num_finder/test_num_finder.py`:** Tests mixed, descending, ascending, and single-element inputs.

---

## 5. How to Run the Tests

The two test projects can be run from their appropriate directories.

### 5.1 Run Calculator Tests

From the repository root:

```bash
cd Lab_01_testing_fundamentals/Calculator_Testing
pytest tests -v
```

Verified result:

```text
12 passed
```

### 5.2 Run NumFinder Tests

From the repository root:

```bash
cd Lab_01_testing_fundamentals/num_finder
pytest -v
```

Verified result:

```text
4 passed
```

> The commands above should match the folder names and import paths used in the actual repository.

---

## 6. Test Execution Summary

The tests were verified separately for each project.

| Test Area          |        Result |
| ------------------ | ------------: |
| Calculator Testing |     12 passed |
| NumFinder Testing  |      4 passed |
| **Total**          | **16 passed** |

The Calculator Testing and NumFinder tests pass when executed from their appropriate project directories.

---

## 7. Testing Concepts Practiced

### AAA Pattern

I practiced organizing a test using:

```text
Arrange → Act → Assert
```

This separates test setup, the operation being tested, and the expected result.

### Testing Different Inputs

The NumFinder tests demonstrate that different input orders can reveal different program behavior.

### Edge Case Testing

The single-element NumFinder test checks an edge case where the same value must be both the smallest and largest.

### Exception Testing

The calculator tests demonstrate how `pytest.raises()` can be used to verify expected exceptions.

### Descriptive Tests

The test function names describe the behavior being checked, making the purpose of each test easier to understand.

### Regression Testing

The descending-list NumFinder test helps detect the original `if / elif` logic defect after the code has been corrected.

---

## 8. Learning Outcomes

After completing this laboratory, I can:

* Write basic automated tests using `pytest`.
* Organize tests using the Arrange, Act, Assert pattern.
* Create test cases for different input conditions.
* Identify how an `if / elif` logic problem can be exposed by a suitable test case.
* Test both successful results and expected exceptions.
* Use pytest output to check whether tests pass or fail.
* Understand why different test inputs are needed to check different behaviors.

Overall, this laboratory introduced the basic process of writing automated tests and showed how carefully selected test cases can reveal problems that may not appear during a simple test.
