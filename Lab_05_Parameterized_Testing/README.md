# Lab 05: Parameterized Testing with Pytest

## Course Information

| Item            | Information                        |
| :-------------- | :--------------------------------- |
| **Course**      | 192-211 Automated Software Testing |
| **Student**     | Thida Khaing                       |
| **Student ID**  | 6705140024                         |
| **Lab**         | Lab 05 — Parameterized Testing     |

---

## Overview

This lab demonstrates how to use **parameterized testing in Pytest** to test multiple input values with a single test function. Instead of writing separate test functions for every test case, `@pytest.mark.parametrize` allows us to define multiple inputs and expected results efficiently.

The lab also covers testing invalid inputs, generating readable test IDs, combining multiple parameters, and marking tests with expected failures using `pytest.mark.xfail`.

## Directory Structure

```text
Lab_05_parameterized_testing/
├── mathutils.py
├── test_param.py
├── test_factorial.py
├── test_multi.py
├── discount.py
├── test_discount.py
├── test_discount_errors.py
├── test_default_ids.py
├── test_custom_ids.py
├── test_param_ids.py
├── test_param_marks.py
└── README.md
```

## Modules and Test Specifications

### 1. Basic Parameterized Testing

**Files:** `mathutils.py`, `test_param.py`, `test_factorial.py`

- **`mathutils.py`**: Contains the `is_even(n)` function to check whether a number is even and the `factorial(n)` function to calculate a factorial. Negative factorial inputs raise a `ValueError`.
- **`test_param.py`**: Tests even and odd numbers using `@pytest.mark.parametrize`.
- **`test_factorial.py`**: Tests factorial calculations for inputs from 0 to 5, including the special case `factorial(0) = 1`.

### 2. Multiple Parameters and Discount Testing

**Files:** `test_multi.py`, `discount.py`, `test_discount.py`, `test_discount_errors.py`

- **`test_multi.py`**: Uses stacked `@pytest.mark.parametrize` decorators to test combinations of two parameters, `x` and `y`. With three `x` values and two `y` values, Pytest generates six test cases.
- **`discount.py`**: Contains the `apply_discount(price, percent)` function, which calculates the final price after applying a discount. It raises a `ValueError` if the discount percentage is below 0 or above 100.
- **`test_discount.py`**: Tests valid discount percentages, including 0%, 10%, 20%, 50%, and 100%.
- **`test_discount_errors.py`**: Tests invalid discount percentages, including negative values and values greater than 100%, to verify that the function raises a `ValueError`.

### 3. Custom Test IDs

**Files:** `test_default_ids.py`, `test_custom_ids.py`, `test_param_ids.py`

- **`test_default_ids.py`**: Demonstrates Pytest's default test IDs when parameterizing test cases with user data.
- **`test_custom_ids.py`**: Uses the `ids` argument to assign descriptive names, such as `alice-adult` and `bob-adult`, to test cases.
- **`test_param_ids.py`**: Uses `pytest.param()` with the `id` argument to label discount test cases as `no_discount`, `half_off`, and `free`.

Custom IDs make test output easier to read and help identify individual test cases when a test fails.

### 4. Expected Failures

**File:** `test_param_marks.py`

- Uses `pytest.mark.xfail` to mark a test case as an expected failure.
- Tests the square of the numbers 2, 3, and 5 against their expected results.
- The test case for `5 ** 2` expects `20`, but the actual result is `25`. Pytest reports this case as `XFAIL` because the failure is expected.

An `XFAIL` is not the same as a passed test. It indicates that a test failed as expected, rather than producing an unexpected failure.

## How to Run the Tests

Run the commands below from the `Lab_05_parameterized_testing` directory.

**Run all tests:**

```bash
pytest -v
```

**Run individual test files:**

```bash
pytest test_param.py -v
pytest test_factorial.py -v
pytest test_discount.py -v
pytest test_discount_errors.py -v
pytest test_multi.py -v -s
pytest test_default_ids.py -v
pytest test_custom_ids.py -v
pytest test_param_ids.py -v
pytest test_param_marks.py -v
```

The `-v` option displays detailed test results. The `-s` option allows printed output from the test functions to appear in the terminal.

## Verified Test Summary

The following results summarize the test execution recorded for this lab.

| **Test File** | **Total Cases** | **Passed** | **Expected Failures (XFAIL)** | **Failed** |
|---|---:|---:|---:|---:|
| `test_param.py` | 10 | 10 | 0 | 0 |
| `test_factorial.py` | 6 | 6 | 0 | 0 |
| `test_discount.py` | 5 | 5 | 0 | 0 |
| `test_discount_errors.py` | 4 | 4 | 0 | 0 |
| `test_multi.py` | 6 | 6 | 0 | 0 |
| `test_default_ids.py` | 2 | 2 | 0 | 0 |
| `test_custom_ids.py` | 2 | 2 | 0 | 0 |
| `test_param_ids.py` | 3 | 3 | 0 | 0 |
| `test_param_marks.py` | 3 | 2 | 1 | 0 |
| **Total** | **41** | **40** | **1** | **0** |

**Summary:** 41 test cases were executed: 40 passed, 1 was reported as an expected failure (`XFAIL`), and 0 unexpected failures were reported.

## Key Learning Outcomes

After completing this lab, I learned how to:

- Use `@pytest.mark.parametrize` to test multiple inputs with one test function.
- Test both valid and invalid inputs, including checking for expected exceptions.
- Combine multiple parameter sets using stacked parameterization decorators.
- Use default and custom test IDs to make test reports easier to understand.
- Use `pytest.param()` to assign IDs to individual test cases.
- Use `pytest.mark.xfail` to document a test that is expected to fail.
- Run individual test files and interpret Pytest's test results.

## Conclusion

This lab helped me understand how parameterized testing makes automated testing more efficient, organized, and maintainable. By testing multiple input values with fewer test functions, I can reduce repetitive code and improve test coverage. I also learned how custom test IDs improve readability and how expected-failure markers help document known issues in a test suite.