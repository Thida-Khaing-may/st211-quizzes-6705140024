# Calculator Testing — Fundamental Unit Testing with Pytest

## Course Information

| Item            | Information                                                        |
| :-------------- | :----------------------------------------------------------------- |
| **Course**      | 192-211 Automated Software Testing                                 |
| **Student**     | Thida Khaing                                                       |
| **Student ID**  | 6705140024                                                         |
| **Lab Topic**   | Fundamental Unit Testing, AAA Pattern, Exceptions & Output Capture |
| **Institution** | Siam University                                                    |

---

## 1. Overview

This laboratory introduces the fundamentals of automated unit testing using Python and `pytest`.

The exercises use a simple calculator module containing four arithmetic operations:

* `add()`
* `subtract()`
* `multiply()`
* `divide()`

The tests demonstrate how to verify normal functionality, organize tests using the **Arrange-Act-Assert (AAA)** pattern, check expected exceptions, identify a deliberately failing test, and capture terminal output.

The lab also includes simple assertion examples using numbers, strings, and lists to practice basic `pytest` assertions.

---

## 2. Project Structure

```text
Calculator_Testing/
│
├── README.md
│
├── src/
│   └── calculator.py
│
└── tests/
    ├── test_calculator.py
    ├── test_exceptions.py
    ├── test_failing.py
    ├── test_first.py
    └── test_output.py
```

### File Description

| File                       | Purpose                                                                                     |
| :------------------------- | :------------------------------------------------------------------------------------------ |
| `src/calculator.py`        | Contains the `add`, `subtract`, `multiply`, and `divide` functions.                         |
| `tests/test_calculator.py` | Tests the basic calculator operations and demonstrates the AAA pattern.                     |
| `tests/test_exceptions.py` | Verifies that division by zero raises the expected `ValueError`.                            |
| `tests/test_failing.py`    | Contains a deliberately failing test example to demonstrate how pytest reports failures.    |
| `tests/test_first.py`      | Contains simple assertion examples using arithmetic, strings, and lists.                    |
| `tests/test_output.py`     | Demonstrates a test that prints a value to the terminal while checking the expected result. |

---

# 3. Calculator Functions

The calculator module provides four basic arithmetic functions.

### `add(a, b)`

Returns the sum of two values.

```python
def add(a, b):
    return a + b
```

Example:

```text
add(2, 3) → 5
```

### `subtract(a, b)`

Returns the difference between two values.

```python
def subtract(a, b):
    return a - b
```

Example:

```text
subtract(10, 4) → 6
```

### `multiply(a, b)`

Returns the product of two values.

```python
def multiply(a, b):
    return a * b
```

Example:

```text
multiply(3, 4) → 12
```

### `divide(a, b)`

Returns the result of division.

The function also checks for division by zero. If `b` is `0`, it raises a `ValueError`.

```python
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

Example:

```text
divide(10, 2) → 5
divide(10, 0) → ValueError
```

---

# 4. Test Design and Exercise Breakdown

## 4.1 Basic Calculator Testing

The `test_calculator.py` file tests the four arithmetic operations.

### Addition

```python
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
```

These assertions check different input situations:

| Input    | Expected Result |
| :------- | :-------------- |
| `2 + 3`  | `5`             |
| `-1 + 1` | `0`             |
| `0 + 0`  | `0`             |

This gives more coverage than testing only one normal positive-value example.

### Subtraction

```python
def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(0, 5) == -5
```

The tests check both a normal subtraction and a case that produces a negative result.

### Multiplication

```python
def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(5, 0) == 0
```

The second assertion verifies the important zero case.

### Division

```python
def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
```

These tests verify normal division using values that produce exact results.

---

# 4.2 Arrange-Act-Assert (AAA) Pattern

The **Arrange-Act-Assert (AAA)** pattern provides a clear structure for writing tests.

| Stage       | Purpose                                | Example                                    |
| :---------- | :------------------------------------- | :----------------------------------------- |
| **Arrange** | Prepare the input and test conditions. | Create `first_number` and `second_number`. |
| **Act**     | Execute the function being tested.     | Call `add(first_number, second_number)`.   |
| **Assert**  | Verify the actual result.              | Check that the result equals `350`.        |

### Example from This Lab

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

### Testing Logic

The test first prepares the two input values:

```text
first_number = 100
second_number = 250
```

This is the **Arrange** stage.

Next, the `add()` function is called:

```text
result = add(100, 250)
```

This is the **Act** stage.

Finally, the result is compared with the expected value:

```text
350 == 350
```

This is the **Assert** stage.

Separating these three stages makes the test easier to read and understand.

---

# 4.3 Testing Exceptions with `pytest.raises`

Not every test checks for a normal return value. Some tests need to verify that a program correctly handles invalid input.

In this lab, division by zero should raise a `ValueError`.

The `pytest.raises()` context manager is used to test this behavior.

```python
def test_divide_by_zero_raises():
    with pytest.raises(ValueError):
        divide(10, 0)
```

This test passes only when `divide(10, 0)` raises a `ValueError`.

If no exception is raised, pytest reports the test as failed.

---

## 4.4 Checking the Exception Message

The lab also checks that the exception contains the expected message.

```python
def test_divide_by_zero_message():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(5, 0)
```

This verifies two things:

1. A `ValueError` is raised.
2. The error message contains:

```text
Cannot divide by zero
```

### Why Test the Message?

Checking only the exception type confirms that an error occurred, but checking the message provides additional verification that the program is reporting the intended error condition.

---

# 4.5 Demonstrating a Failing Test

The `test_failing.py` file intentionally contains a test that does not match the actual result.

```python
from src.calculator import add

def test_this_will_fail():
    result = add(2, 2)
    assert result == 4
```

In the code provided, this test actually evaluates to:

```text
add(2, 2) → 4
```

Therefore, **as currently written, this test will pass**, despite its name `test_this_will_fail`.

The test name does not determine whether a test passes or fails. Pytest evaluates the assertion result.

For example, if the assertion were:

```python
assert result == 5
```

then the test would fail because:

```text
Actual result:   4
Expected result: 5
```

### Main Lesson

A test is considered failed when its assertion does not match the actual behavior. The name of the test does not control the result.

---

# 4.6 Basic Assertions

The `test_first.py` file contains simple examples of pytest assertions.

### Numeric Assertion

```python
def test_addition():
    assert 1 + 1 == 2
```

This checks a basic arithmetic expression.

### String Assertion

```python
def test_string():
    assert "hello".upper() == "HELLO"
```

This verifies that the string is converted to uppercase correctly.

### List Assertion

```python
def test_list_length():
    fruits = ["apple", "banana", "cherry"]
    assert len(fruits) == 3
```

This verifies the number of elements in a list.

These examples demonstrate that pytest's `assert` statement can be used to check many different types of Python values.

---

# 4.7 Testing and Printing Output

The `test_output.py` file demonstrates a test that prints information to the terminal.

```python
def test_with_print():
    value = 42
    print(f"The value is {value}")
    assert value == 42
```

The assertion checks that:

```text
value == 42
```

The `print()` statement produces:

```text
The value is 42
```

However, pytest normally captures standard output during test execution.

To display the printed output in the terminal, the `-s` option can be used:

```bash
pytest -s
```

The same option can be combined with verbose mode:

```bash
pytest -v -s
```

Here:

* `-v` means **verbose output**.
* `-s` disables pytest's output capture so that `print()` output is displayed.

---

# 5. Running the Tests

All commands should be executed from the `Calculator_Testing` directory.

## 5.1 Run All Tests

```bash
pytest
```

This discovers and executes the test files in the project.

---

## 5.2 Run Tests in Verbose Mode

```bash
pytest -v
```

The `-v` option provides more detailed information, including the name and result of each test.

Example:

```text
tests/test_calculator.py::test_add PASSED
tests/test_calculator.py::test_subtract PASSED
tests/test_exceptions.py::test_divide_by_zero_raises PASSED
```

The exact number of tests depends on the files currently included in the project.

---

## 5.3 Run the Calculator Tests Only

```bash
pytest tests/test_calculator.py -v
```

This runs the tests for the four calculator operations and the AAA example.

---

## 5.4 Run the Exception Tests

```bash
pytest tests/test_exceptions.py -v
```

This runs the tests related to division-by-zero error handling.

---

## 5.5 Run the Basic Assertion Tests

```bash
pytest tests/test_first.py -v
```

This runs the arithmetic, string, and list assertion examples.

---

## 5.6 Run the Output Test

```bash
pytest tests/test_output.py -v -s
```

The `-s` option allows the `print()` output to appear in the terminal.

Expected printed output includes:

```text
The value is 42
```

---

## 5.7 Run One Specific Test

A single test can also be executed by specifying the test file and function name.

For example:

```bash
pytest tests/test_calculator.py::test_add -v
```

This is useful when debugging or checking one particular test without running the entire test suite.

---

# 6. Important Pytest Concepts Practiced

## Assertions

An assertion compares the actual result with the expected result.

```python
assert add(2, 3) == 5
```

If the condition is true, the test passes.

If the condition is false, the test fails.

---

## Exception Testing

`pytest.raises()` verifies that a specific exception occurs.

```python
with pytest.raises(ValueError):
    divide(10, 0)
```

This is useful when invalid input is expected to produce an error.

---

## AAA Pattern

The AAA pattern organizes a test into:

```text
Arrange → Act → Assert
```

This provides a simple and readable structure for unit tests.

---

## Verbose Test Execution

The `-v` option provides detailed test information:

```bash
pytest -v
```

This makes it easier to identify which individual tests passed or failed.

---

## Output Capture

Pytest captures standard output by default.

The `-s` option disables this capture:

```bash
pytest -s
```

This allows `print()` statements to appear directly in the terminal.

---

# 7. Expected Test Behavior

The main calculator and exception tests are designed to pass when the calculator implementation behaves as expected.

The important behaviors are:

| Test Area        | Expected Behavior                                |
| :--------------- | :----------------------------------------------- |
| Addition         | Correctly returns the sum                        |
| Subtraction      | Correctly returns the difference                 |
| Multiplication   | Correctly returns the product                    |
| Division         | Correctly returns the quotient                   |
| Division by zero | Raises `ValueError`                              |
| Error message    | Contains `Cannot divide by zero`                 |
| Basic assertions | Correct numeric, string, and list results        |
| Output test      | Prints the value when output capture is disabled |

One important observation from this lab is that `test_failing.py` is named as a failing-test example, but the current assertion `assert result == 4` is correct for `add(2, 2)`. Therefore, it will pass unless the assertion or calculator behavior is changed.

---

# 8. What I Learned

Through this laboratory, I practiced the basic workflow of automated unit testing with `pytest`.

### 1. Writing Unit Tests

I learned how to import functions from a source module and test their behavior with assertions.

### 2. Using the AAA Pattern

I learned how to separate a test into:

```text
Arrange → Act → Assert
```

This makes the test logic easier to follow.

### 3. Testing Exceptions

I learned how to use `pytest.raises()` to verify that invalid operations produce the expected exception.

### 4. Checking Error Messages

I learned that exception tests can also verify the error message, not only the exception type.

### 5. Understanding Test Results

I learned that pytest determines whether a test passes or fails based on the actual assertion result, not the test function's name.

### 6. Using Pytest Command-Line Options

I practiced using:

```bash
pytest
pytest -v
pytest -s
```

These options provide different levels of information when running tests.

### 7. Understanding Output Capture

I learned that pytest normally captures `print()` output and that `-s` can be used when I need to see the output directly in the terminal.

---

# 9. Conclusion

This laboratory provided practical experience with the basic components of automated unit testing.

The calculator example helped me practice testing normal functionality, while the division-by-zero tests demonstrated how to verify error handling. The AAA example showed how a test can be organized into clear stages, and the basic assertion and output exercises provided additional practice with pytest behavior.

Overall, the lab helped me understand that writing tests involves more than simply checking whether code returns the expected value. Tests can also verify **error conditions, exception messages, test structure, and program output**, providing a foundation for more advanced automated testing techniques.
