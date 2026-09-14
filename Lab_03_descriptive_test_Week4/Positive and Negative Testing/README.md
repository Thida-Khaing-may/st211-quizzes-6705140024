# Week 4: Positive and Negative Testing

- **Course:** 192-211 Automated Software Testing
- **Student:** Thida Khaing 6705140024
- **Lab:** Week 4 — Descriptive Testing
- **Exercise:** Positive and Negative Testing
- **Files Used:**
  - `validators.py`
  - `test_positive.py`
  - `test_negative.py`

---

## 1. Exercise Title

**Week 4 — Automated Software Testing: Positive and Negative Testing**

This lab exercise focuses on testing validation logic across two essential data fields: email addresses and user ages. Using Python and `pytest`, the exercise demonstrates how to design, organize, and evaluate both positive (valid) and negative (invalid) test scenarios across three files:
- `validators.py` (Implementation under test)
- `test_positive.py` (Positive test suite)
- `test_negative.py` (Negative test suite)

---

## 2. Purpose of the Exercise

In software development, **validation** is the process of verifying that incoming data conforms to required business rules, syntactical formats, and safe boundaries before the program processes or stores it.

### Why Testing Only Valid Inputs Is Not Enough
Testing only valid data ("happy paths") proves only that a system functions when users provide perfect input. However, in real-world applications, systems encounter unexpected, malformed, or hostile inputs (such as typos, missing symbols, wrong data types, or out-of-range numbers). If validation fails or behaves unpredictably, an application might crash, corrupt database records, or introduce security vulnerabilities.

### What Positive and Negative Testing Verify
- **Positive Testing** verifies that legitimate, well-formed data is successfully accepted by the system:
  $$\text{Valid input} \longrightarrow \text{system should accept it (return True)}$$
- **Negative Testing** verifies that malformed, out-of-range, or incorrect data types are properly intercepted and rejected:
  $$\text{Invalid input} \longrightarrow \text{system should reject it correctly}$$

### Checking the Correct Type of Error
Negative testing does not simply check that "an error occurred." It verifies that the system produces the **exact, expected exception type** (`TypeError` vs. `ValueError`) and rejects the input for the right reason.

---

## 3. Testing Logic / Test Design

The tests in this exercise follow a structured, disciplined test design workflow:

$$\textbf{Requirement / Validation Rule} \longrightarrow \textbf{Choose an Input} \longrightarrow \textbf{Determine Expected Behavior} \longrightarrow \textbf{Write Assertion / Exception Check} \longrightarrow \textbf{Run the Test}$$

### Applying Test Design to the Actual Rules

1. **Rule: Email must strictly match the specified regular expression.**
   - *Design Decision (Positive):* Supply email strings containing legitimate features allowed by the regex, such as two-level institutional domains (`student@siam.ac.th`), subdomains (`user@email.example.com`), numeric characters (`student123@gmail.com`), and dot separators (`first.last@gmail.com`).
   - *Expected Behavior:* Each must return `True`.
   - *Design Decision (Negative):* Choose inputs that violate one specific regex element at a time (e.g., omitting `@`, omitting domain, omitting username, omitting dot, using a single-letter TLD, embedding spaces, omitting extension, or providing an empty string `""`).
   - *Expected Behavior:* Each must raise `ValueError`.

2. **Rule: Age must be of integer type.**
   - *Design Decision (Negative):* Supply inputs of non-integer data types such as a string (`"twenty"`), a floating-point number (`25.5`), a `None` value (`None`), and a list (`[25]`).
   - *Expected Behavior:* Each must raise `TypeError`.

3. **Rule: Age must be an integer between 0 and 150 (inclusive).**
   - *Design Decision (Positive):* Test nominal valid values (`25`) as well as the exact boundary limits (`0` and `150`).
   - *Expected Behavior:* Each must return `True`.
   - *Design Decision (Negative):* Test integer values immediately outside the allowed range: one below the minimum (`-5`) and one above the maximum (`151`).
   - *Expected Behavior:* Each must raise `ValueError`.

---

## 4. `validators.py`

The file `validators.py` contains the core validation logic used in this exercise:

```python
import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        raise ValueError(f"Invalid email:{email}")
    return True

def validate_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0 or age > 150:
        raise ValueError("Age must be 0-150")
    return True
```

### Function Summary

| Function | Input | Validation Rule | Behavior When Valid | Behavior When Invalid | Exception Raised |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `validate_email(email)` | `email` (str) | Must match regex pattern | Returns `True` | Fails regex match | `ValueError` |
| `validate_age(age)` | `age` (any) | 1. Must be `int`<br>2. Must be $0 \le \text{age} \le 150$ | Returns `True` | 1. Non-integer type<br>2. Outside $0–150$ | 1. `TypeError`<br>2. `ValueError` |

---

## 5. `validate_email()`

The email validation function relies on Python's `re.match()` to evaluate candidate strings against a strict regular expression:

```python
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
```

### Regular Expression Breakdown

| Regex Part | Meaning | What It Allows |
| :--- | :--- | :--- |
| `^` | Start anchor | Asserts that matching begins at the first character of the string. |
| `[a-zA-Z0-9._%+-]+` | Username / local part | One or more uppercase/lowercase letters, digits, dots, underscores, percent signs, plus signs, or hyphens. |
| `@` | Separator | Exactly one literal `@` character separating the local part and the domain. |
| `[a-zA-Z0-9.-]+` | Domain name | One or more uppercase/lowercase letters, digits, dots (for subdomains), or hyphens. |
| `\.` | Dot separator | A required literal period separating the domain name from the top-level domain. |
| `[a-zA-Z]{2,}` | Top-Level Domain (TLD) | At least 2 alphabetic letters (e.g., `th`, `com`, `org`, `edu`). Numeric digits or 1-letter extensions are disallowed. |
| `$` | End anchor | Asserts that matching ends at the final character. No trailing characters or trailing whitespace are permitted. |

### Return and Exception Contract
- **Accepted (Valid):** If `re.match(pattern, email)` succeeds, the function returns `True`.
- **Rejected (Invalid):** If `re.match()` fails to match the entire pattern, the condition `if not re.match(...)` triggers and raises:
  ```python
  raise ValueError(f"Invalid email:{email}")
  ```

---

## 6. `validate_age()`

The `validate_age(age)` function executes a two-step validation pipeline in a deliberate order:

### Step 1 — Type Checking
```python
if not isinstance(age, int):
    raise TypeError("Age must be an integer")
```
Before checking numeric boundaries, the function validates the data type. In Python, comparing a string or a list to an integer using comparison operators (`<` or `>`) can raise unhandled errors or produce unexpected behavior. Therefore, non-integer inputs are intercepted first:
- Strings like `"twenty"` are rejected.
- Floating-point values like `25.5` are rejected (age in this design must be a whole integer).
- `None` is rejected.
- Composite collections like `[25]` are rejected.

All of these raise a `TypeError`.

### Step 2 — Range Checking
```python
if age < 0 or age > 150:
    raise ValueError("Age must be 0-150")
```
Once the input is confirmed to be an integer, the function inspects its value:
- `0` is accepted (minimum boundary).
- `150` is accepted (maximum boundary).
- Values below `0` (e.g., `-5`) are rejected.
- Values above `150` (e.g., `151`) are rejected.

Any integer outside $[0, 150]$ raises a `ValueError`.

### Type Validation vs. Range/Value Validation

| Validation Phase | Question Asked | Checks Performed On | Exception Raised |
| :--- | :--- | :--- | :--- |
| **Type Validation** | *"Is the data in the right representation?"* | Data structure / type (`int`, `str`, etc.) | `TypeError` |
| **Range / Value Validation** | *"Is the value within acceptable limits?"* | Magnitude / numeric value | `ValueError` |

---

## 7. `TypeError` vs. `ValueError`

The tests in this module clearly illustrate the standard Python convention for exception types:

### `TypeError`: Wrong Data Type
Raised when an operation or function receives an argument of an inappropriate data type:
- `"twenty"` &rarr; `str` instead of `int`
- `25.5` &rarr; `float` instead of `int`
- `None` &rarr; `NoneType` instead of `int`
- `[25]` &rarr; `list` instead of `int`

### `ValueError`: Wrong Value or Format
Raised when an operation or function receives an argument that has the correct general type, but an inappropriate or out-of-range value:
- `-5` &rarr; correct type (`int`), but below minimum boundary ($0$)
- `151` &rarr; correct type (`int`), but above maximum boundary ($150$)
- `"notanemail.com"` &rarr; correct type (`str`), but violates the email format specification

$$\textbf{Wrong Type} \longrightarrow \text{TypeError}$$
$$\textbf{Correct Type, Invalid Value/Format} \longrightarrow \text{ValueError}$$

---

## 8. Positive Testing — `test_positive.py`

> **Positive tests check that valid inputs are accepted and produce the expected successful result (`True`).**

The test file `test_positive.py` imports `validate_email` and `validate_age` from `validators.py` and implements 6 test functions verifying the happy path.

---

## 9. Positive Email Tests

### 1. `test_valid_email_accepted`
- **Input:** `"student@siam.ac.th"`
- **Why this input was chosen:** Tests an academic/institutional email address with a multi-level country-code domain (`siam.ac.th`).
- **Expected behavior:** The regex accepts the domain dots and the 2-letter country code extension (`th`), returning `True`.
- **How the test verifies it:**
  ```python
  assert validate_email("student@siam.ac.th") is True
  ```
  The `assert ... is True` statement verifies both truthiness and exact boolean identity.

### 2. `test_valid_email_with_subdomain`
- **Input:** `"user@email.example.com"`
- **Why this input was chosen:** Tests that email addresses with subdomains (`email.example.com`) match the `[a-zA-Z0-9.-]+` domain pattern.
- **Expected behavior:** The function accepts multiple domain segments separated by dots and returns `True`.
- **How the test verifies it:**
  ```python
  assert validate_email("user@email.example.com") is True
  ```

### 3. `test_email_with_numbers`
- **Input:** `"student123@gmail.com"`
- **Why this input was chosen:** Tests that numeric digits (`0-9`) in the local username part are permitted by `[a-zA-Z0-9._%+-]+`.
- **Expected behavior:** The username `student123` matches successfully, returning `True`.
- **How the test verifies it:**
  ```python
  assert validate_email("student123@gmail.com") is True
  ```

### 4. `test_email_with_dot`
- **Input:** `"first.last@gmail.com"`
- **Why this input was chosen:** Tests that dot characters (`.`) inside the local username part are accepted.
- **Expected behavior:** The username `first.last` matches successfully, returning `True`.
- **How the test verifies it:**
  ```python
  assert validate_email("first.last@gmail.com") is True
  ```

---

## 10. Positive Age Tests

### 1. `test_valid_age_accepted`
- **Input:** `25`
- **Why this input was chosen:** Represents a nominal valid age well within the middle of the valid range ($0–150$).
- **Expected behavior:** `isinstance(25, int)` is `True` and $0 \le 25 \le 150$, returning `True`.
- **How the test verifies it:**
  ```python
  assert validate_age(25) is True
  ```

### 2. `test_boundary_ages_accepted`
- **Inputs:** `0` and `150`
- **Why these inputs were chosen:** Represents the exact lower and upper boundary limits of the allowed age range.
- **Expected behavior:** Both `0` and `150` satisfy the condition $0 \le \text{age} \le 150$ and return `True`.
- **How the test verifies it:**
  ```python
  assert validate_age(0) is True
  assert validate_age(150) is True
  ```

### Boundary Testing
> **Boundary Testing** focuses on the extreme edges of input domains where software defects and off-by-one errors ($<$ vs. $\le$, $>$ vs. $\ge$) are most commonly introduced.

For this implementation:
```text
Allowed Range: [0, 150] (inclusive)

  ... -1  |  0 ..................... 150  |  151 ...
  Invalid | Valid Minimum   Valid Maximum | Invalid
```
- `0` is the **valid minimum boundary**.
- `150` is the **valid maximum boundary**.

The positive test `test_boundary_ages_accepted` proves that both extreme boundaries are correctly included.

---

## 11. Negative Testing — `test_negative.py`

> **Negative tests intentionally provide invalid input and verify that the program rejects it in the expected way.**

### Testing Failure vs. Testing the Correct Exception
In automated software testing, it is not enough to verify merely that invalid input "fails" or returns an error. A robust negative test must verify that:
1. An exception was actually raised.
2. The exception raised was the **correct and intended exception class** (`ValueError` for format/range issues, `TypeError` for data type violations).
3. The program does not crash unexpectedly with an unhandled runtime error.

---

## 12. `pytest.raises()`

In `test_negative.py`, all exception tests use pytest's built-in context manager:

```python
with pytest.raises(ValueError):
    validate_email("notanemail.com")
```

### How `pytest.raises()` Works
1. **Purpose:** It wraps a block of code and listens for a specific exception type.
2. **When the expected exception is raised:** Pytest intercepts the exception, suppresses it, and marks that assertion as **PASSED**.
3. **When no exception is raised:** If the code inside the block executes without error, pytest fails the test with a message indicating that the expected exception was not raised (e.g., `Failed: DID NOT RAISE <class 'ValueError'>`).
4. **When a different exception is raised:** If an unexpected exception occurs (e.g., code raises `KeyError` instead of `ValueError`), pytest does not suppress it and reports the test as **FAILED** or **ERROR**.

---

## 13. Negative Email Tests

The file `test_negative.py` tests 8 distinct email syntax violations against `validate_email()`. Each test uses `with pytest.raises(ValueError):`.

| Test Name | Input | What Is Wrong | Regex Rule Violated | Expected Exception |
| :--- | :--- | :--- | :--- | :--- |
| `test_email_without_at_rejected` | `"notanemail.com"` | Missing `@` symbol | `@` separator is required | `ValueError` |
| `test_email_without_domain_rejected` | `"user@"` | No domain name after `@` | `[a-zA-Z0-9.-]+` requires at least 1 character | `ValueError` |
| `test_email_without_username_rejected` | `"@gmail.com"` | No username before `@` | `[a-zA-Z0-9._%+-]+` requires at least 1 character | `ValueError` |
| `test_email_without_dot_rejected` | `"user@gmail"` | Missing dot separating domain and TLD | Literal `\.` is required | `ValueError` |
| `test_email_with_one_letter_extension_rejected` | `"user@gmail.c"` | TLD has only 1 letter (`.c`) | `[a-zA-Z]{2,}` requires at least 2 characters | `ValueError` |
| `test_email_with_space_rejected` | `"user name@gmail.com"` | Space character in username | Spaces are not in `[a-zA-Z0-9._%+-]` | `ValueError` |
| `test_email_without_extension_rejected` | `"user@gmail."` | Trailing dot with no TLD characters | `[a-zA-Z]{2,}` requires at least 2 letters after `\.` | `ValueError` |
| `test_empty_email_rejected` | `""` | Completely empty string | `^` and `$` require the full pattern; empty fails | `ValueError` |

Each test confirms that `re.match()` returns `None`, triggering `raise ValueError(...)`.

---

## 14. Negative Age Tests

The negative age tests in `test_negative.py` are divided into out-of-range value errors and invalid data type errors.

### A. Out-of-Range Values (`ValueError`)

These tests verify that integer values beyond the $[0, 150]$ interval trigger a `ValueError`:

1. **`test_negative_age_rejected`**
   - **Input:** `-5`
   - **Rule Violated:** Age cannot be less than 0 (`age < 0`).
   - **Expected Exception:** `ValueError("Age must be 0-150")`
   - **Verification:** `with pytest.raises(ValueError): validate_age(-5)`

2. **`test_age_over_150_rejected`**
   - **Input:** `151`
   - **Rule Violated:** Age cannot exceed 150 (`age > 150`).
   - **Expected Exception:** `ValueError("Age must be 0-150")`
   - **Verification:** `with pytest.raises(ValueError): validate_age(151)`

### B. Wrong Data Types (`TypeError`)

These tests verify that non-integer inputs trigger a `TypeError` in Step 1 before any range comparisons occur:

1. **`test_age_as_string_rejected`**
   - **Input:** `"twenty"`
   - **Rule Violated:** Input is a `str`, not an `int`.
   - **Expected Exception:** `TypeError("Age must be an integer")`
   - **Verification:** `with pytest.raises(TypeError): validate_age("twenty")`

2. **`test_age_as_float_rejected`**
   - **Input:** `25.5`
   - **Rule Violated:** Input is a `float`, not an `int`.
   - **Expected Exception:** `TypeError("Age must be an integer")`
   - **Verification:** `with pytest.raises(TypeError): validate_age(25.5)`

3. **`test_age_as_none_rejected`**
   - **Input:** `None`
   - **Rule Violated:** Input is `NoneType`, not an `int`.
   - **Expected Exception:** `TypeError("Age must be an integer")`
   - **Verification:** `with pytest.raises(TypeError): validate_age(None)`

4. **`test_age_as_list_rejected`**
   - **Input:** `[25]`
   - **Rule Violated:** Input is a `list`, not an `int`.
   - **Expected Exception:** `TypeError("Age must be an integer")`
   - **Verification:** `with pytest.raises(TypeError): validate_age([25])`

---

## 15. Positive vs. Negative Testing Comparison

| Aspect | Positive Testing | Negative Testing |
| :--- | :--- | :--- |
| **Input** | Valid, well-formed | Invalid, malformed, or wrong type |
| **Goal** | Confirm acceptance | Confirm safe rejection |
| **Expected Behavior** | Returns `True` | Raises specific expected exception |
| **Email Example** | `validate_email("student@siam.ac.th")` | `validate_email("notanemail.com")` |
| **Age Range Example** | `validate_age(25)` | `validate_age(-5)` |
| **Age Type Example** | `validate_age(0)` | `validate_age("twenty")` |
| **Pytest Tool** | `assert ... is True` | `with pytest.raises(...)` |

---

## 16. Complete Test Mapping Table

Below is the complete mapping of all 20 actual test functions defined in `test_positive.py` and `test_negative.py`:

| # | Test Function | File | Function Tested | Input | Expected Result | Exception |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `test_valid_email_accepted` | `test_positive.py` | `validate_email` | `"student@siam.ac.th"` | Returns `True` | None |
| 2 | `test_valid_email_with_subdomain` | `test_positive.py` | `validate_email` | `"user@email.example.com"` | Returns `True` | None |
| 3 | `test_email_with_numbers` | `test_positive.py` | `validate_email` | `"student123@gmail.com"` | Returns `True` | None |
| 4 | `test_email_with_dot` | `test_positive.py` | `validate_email` | `"first.last@gmail.com"` | Returns `True` | None |
| 5 | `test_valid_age_accepted` | `test_positive.py` | `validate_age` | `25` | Returns `True` | None |
| 6 | `test_boundary_ages_accepted` | `test_positive.py` | `validate_age` | `0` and `150` | Returns `True` | None |
| 7 | `test_email_without_at_rejected` | `test_negative.py` | `validate_email` | `"notanemail.com"` | Rejection | `ValueError` |
| 8 | `test_email_without_domain_rejected` | `test_negative.py` | `validate_email` | `"user@"` | Rejection | `ValueError` |
| 9 | `test_email_without_username_rejected` | `test_negative.py` | `validate_email` | `"@gmail.com"` | Rejection | `ValueError` |
| 10 | `test_email_without_dot_rejected` | `test_negative.py` | `validate_email` | `"user@gmail"` | Rejection | `ValueError` |
| 11 | `test_email_with_one_letter_extension_rejected` | `test_negative.py` | `validate_email` | `"user@gmail.c"` | Rejection | `ValueError` |
| 12 | `test_email_with_space_rejected` | `test_negative.py` | `validate_email` | `"user name@gmail.com"` | Rejection | `ValueError` |
| 13 | `test_email_without_extension_rejected` | `test_negative.py` | `validate_email` | `"user@gmail."` | Rejection | `ValueError` |
| 14 | `test_empty_email_rejected` | `test_negative.py` | `validate_email` | `""` | Rejection | `ValueError` |
| 15 | `test_negative_age_rejected` | `test_negative.py` | `validate_age` | `-5` | Rejection | `ValueError` |
| 16 | `test_age_over_150_rejected` | `test_negative.py` | `validate_age` | `151` | Rejection | `ValueError` |
| 17 | `test_age_as_string_rejected` | `test_negative.py` | `validate_age` | `"twenty"` | Rejection | `TypeError` |
| 18 | `test_age_as_float_rejected` | `test_negative.py` | `validate_age` | `25.5` | Rejection | `TypeError` |
| 19 | `test_age_as_none_rejected` | `test_negative.py` | `validate_age` | `None` | Rejection | `TypeError` |
| 20 | `test_age_as_list_rejected` | `test_negative.py` | `validate_age` | `[25]` | Rejection | `TypeError` |

---

## 17. How to Run the Tests

From the terminal, navigate to the `Positive and Negative Testing` directory:

```bash
cd "Lab_03_descriptive_test_Week4/Positive and Negative Testing"
```

### 1. Run all tests with verbose output
```bash
pytest -v
```

### 2. Run only positive tests
```bash
pytest test_positive.py -v
```

### 3. Run only negative tests
```bash
pytest test_negative.py -v
```

### Explanation of `-v`
The `-v` flag stands for **verbose**. By default, `pytest` prints only summary characters (e.g., `.` for pass, `F` for fail). Adding `-v` instructs pytest to display the filename, the exact name of every individual test function, and its completion status (`PASSED` or `FAILED`).

---

## 18. Test Result

> Test execution result should be recorded after running pytest.

When executed in a Python environment with pytest installed:
- Pytest discovers all 20 test functions (6 in `test_positive.py` and 14 in `test_negative.py`).
- All valid input assertions evaluate to `True`.
- All invalid input tests successfully trigger the expected `TypeError` or `ValueError` intercepted by `pytest.raises()`.
- Each test runs independently without shared state or side effects.

---

## 19. Key Learning Outcomes

This lab exercise demonstrates the following core software testing concepts:

- **Positive Testing:** Confirming that valid data flows through the application and produces expected successful outcomes.
- **Negative Testing:** Proactively testing with invalid inputs to confirm robust error detection and safe failure modes.
- **Input Validation:** Enforcing format and domain rules before data is accepted by the system.
- **Boundary Testing:** Identifying and testing the exact edge values ($0$ and $150$) of numeric input intervals.
- **Regular Expression Validation:** Verifying that structured string formats (emails) comply with pattern requirements.
- **Exception Testing:** Verifying error conditions using `with pytest.raises(...)`.
- **`TypeError` vs. `ValueError`:** Distinguishing between data type errors and value/range errors in function contracts.
- **Assertions:** Using Python's native `assert ... is True` syntax for clear verification.
- **Designing Tests from Rules:** Systematically selecting test cases based on validation rules rather than random trial-and-error.
- **Choosing Deliberate Test Inputs:** Selecting specific inputs that isolate individual validation rules.

---

## 20. Conclusion

A complete, high-quality automated test suite does not stop at proving that an application functions when used correctly. True software reliability requires verifying that systems gracefully intercept invalid inputs and fail safely with the correct error types.

By organizing tests into positive and negative suites, and systematically designing test cases directly from the validation logic in `validators.py`, this lab establishes a repeatable framework for building robust, defensive, and well-tested software.
