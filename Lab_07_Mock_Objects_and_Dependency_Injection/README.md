# Lab 07 — Mock Objects and Dependency Injection

## Course Information

| Item | Information |
| :--- | :--- |
| **Course** | 192-211 Automated Software Testing |
| **Student** | Thida Khaing |
| **Student ID** | 6705140024 |
| **Lab** | Lab 07 — Mock Objects and Side Effects |

---

## Overview

This laboratory explores how Python's `unittest.mock.Mock` object supports test-driven development and automated unit testing. Mock objects can replace external, unavailable, or non-deterministic dependencies, allowing tests to run without relying on real services.

The exercises demonstrate the differences between `return_value` and `side_effect`, including static return values, exceptions, iterable sequences, and custom callable functions.

## Learning Objectives

By completing this lab, I learned how to:

- Create and configure mock objects using `unittest.mock.Mock`.
- Use `return_value` to provide consistent results across multiple calls.
- Use `side_effect` to raise exceptions.
- Use iterable side effects to return different values on consecutive calls.
- Use callable side effects to process input arguments dynamically.
- Compare different mock configurations in automated tests.
- Verify exceptions using `pytest.raises()`.

## Lab Structure

```text
Lab_07_Mock_Objects_and_Dependency_Injection/
├── payment.py
├── README.md
└── Exercise/
    ├── test_mock_basics.py
    ├── test_return_value.py
    ├── test_side_effect_exception.py
    ├── test_side_effect_list.py
    ├── test_side_effect_function.py
    └── test_comparison.py
```

## Exercise 1: Basic Mock Objects

**File:** `Exercise/test_mock_basics.py`

This exercise explores the basic behavior of mock objects.

Topics covered:

- Configuring a method to return a fixed value.
- Accessing methods that have not been explicitly defined.
- Calling mock methods with positional arguments.
- Assigning and reading custom attributes.

Example:

```python
from unittest.mock import Mock

mock = Mock()
mock.get_data.return_value = "fake data"

assert mock.get_data() == "fake data"
```

## Exercise 2: Using `return_value`

**File:** `Exercise/test_return_value.py`

The `return_value` attribute specifies the value returned whenever a mock method is called.

Topics covered:

- Returning a string such as `"OK"`.
- Returning an integer such as `123`.
- Verifying that repeated calls return the same configured value.

Example:

```python
from unittest.mock import Mock

mock = Mock()
mock.get_status.return_value = "OK"

assert mock.get_status() == "OK"
assert mock.get_status() == "OK"
```

## Exercise 3: Using `side_effect` to Raise Exceptions

**File:** `Exercise/test_side_effect_exception.py`

An exception assigned to `side_effect` is raised when the mock method is called. This makes it possible to test how an application handles errors without depending on a real external service.

Topics covered:

- Raising `ValueError` for invalid credentials.
- Raising `RuntimeError` to simulate an operational failure.
- Checking expected exceptions with `pytest.raises()`.

Example:

```python
import pytest
from unittest.mock import Mock

mock = Mock()
mock.login.side_effect = ValueError("Invalid credentials")

with pytest.raises(ValueError):
    mock.login()
```

## Exercise 4: Using `side_effect` with a List

**File:** `Exercise/test_side_effect_list.py`

When an iterable is assigned to `side_effect`, each call returns the next item in the iterable.

Topics covered:

- Returning `"A"`, `"B"`, and `"C"` on consecutive calls.
- Understanding iterator exhaustion.
- Testing `StopIteration` after all configured values have been consumed.
- Comparing iterable `side_effect` with a list assigned to `return_value`.

Example:

```python
import pytest
from unittest.mock import Mock

mock = Mock()
mock.get_data.side_effect = ["A", "B", "C"]

assert mock.get_data() == "A"
assert mock.get_data() == "B"
assert mock.get_data() == "C"

with pytest.raises(StopIteration):
    mock.get_data()
```

**Important difference:** A list assigned to `return_value` is returned as a complete list on every call. A list assigned to `side_effect` supplies its elements one at a time.

## Exercise 5: Using `side_effect` with a Function

**File:** `Exercise/test_side_effect_function.py`

A callable assigned to `side_effect` runs when the mock method is called. The arguments passed to the mock are forwarded to that callable.

Topics covered:

- Defining a custom function.
- Passing arguments through the mock.
- Returning a calculated result.

Example:

```python
from unittest.mock import Mock

def double(x):
    return x * 2

mock = Mock()
mock.calculate.side_effect = double

assert mock.calculate(5) == 10
```

## Exercise 6: Comparing Mock Behaviors

**File:** `Exercise/test_comparison.py`

This exercise compares different mock configurations.

| Configuration | Behavior |
|---|---|
| `return_value` | Returns the same configured value on repeated calls. |
| `side_effect` with a list | Returns successive items from an iterable. |
| `side_effect` with an exception | Raises the configured exception when called. |
| `side_effect` with a function | Executes the function using the call's arguments. |

The comparison helps demonstrate when each configuration is useful in automated testing.

## Test Execution Summary

The following results should be recorded after running the test suite.

| Test file | Expected test count |
|---|---:|
| `test_mock_basics.py` | 3 |
| `test_return_value.py` | 2 |
| `test_side_effect_exception.py` | 2 |
| `test_side_effect_list.py` | 2 |
| `test_side_effect_function.py` | 1 |
| `test_comparison.py` | 4 |
| **Total** | **14** |

**Test status:** Record the actual pytest results after execution. If all tests pass, report **14 passed**.

## Key Takeaways

- **`return_value`:** Use it when a mock should return a fixed value on every call.
- **`side_effect` with an exception:** Use it to test error-handling behavior.
- **`side_effect` with an iterable:** Use it to simulate changing results across consecutive calls.
- **`side_effect` with a callable:** Use it when the mock's behavior depends on input arguments or custom logic.

## How to Run the Tests

Activate the virtual environment, navigate to the `Lab_07_Mock_Objects_and_Dependency_Injection` directory, and run:

```powershell
pytest Exercise -v -s
```

To run an individual test file:

```powershell
pytest Exercise/test_comparison.py -v -s
```

## Conclusion

This laboratory demonstrates how mock objects can replace dependencies and control their behavior during automated tests. By comparing `return_value` and the different forms of `side_effect`, I gained a better understanding of how to test normal results, changing responses, exceptions, and input-dependent behavior without relying on real external services.
