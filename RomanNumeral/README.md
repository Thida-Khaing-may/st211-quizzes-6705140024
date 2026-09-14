# Lab 01 — Roman Numeral Converter & Unit Testing Basics

## Course Information

| Item           | Information                               |
| :------------- | :---------------------------------------- |
| **Course**     | 192-211 Automated Software Testing        |
| **Student**    | Thida Khaing                              |
| **Student ID** | 6705140024                                |
| **Lab**        | Week 2 — Unit Testing Basics & Edge Cases |

---

## 1. Overview

This laboratory focuses on developing and testing a **Roman numeral converter** using Python and `pytest`.

The main purpose of the project is to verify that Roman numeral strings can be correctly converted into integer values while also detecting invalid Roman numeral formats.

The implementation contains two main functions:

* `convert()` — converts a Roman numeral string into an integer.
* `to_roman()` — converts an integer into a Roman numeral and is used to validate whether the original Roman numeral was written correctly.

The testing focuses on several important areas:

* Correct conversion of standard Roman numeral symbols.
* Correct handling of repeated symbols.
* Correct implementation of additive notation.
* Correct implementation of subtractive notation.
* Detection of invalid Roman numeral combinations.
* Handling of empty and non-string inputs.
* Validation of Roman numeral formatting.
* Testing edge cases and invalid inputs using exception assertions.

The goal is not only to check whether the converter produces the correct answer, but also to verify that it **rejects invalid input appropriately**.

---

## 2. Project Structure

The project is organized as follows:

```text
RomanNumeral/
│
├── source/
│   └── roman.py
│
├── tests/
│   └── test_roman.py
│
└── README.md
```

### File Description

| File                  | Purpose                                                                                       |
| :-------------------- | :-------------------------------------------------------------------------------------------- |
| `source/roman.py`     | Contains the `convert()` and `to_roman()` functions and the command-line converter.           |
| `tests/test_roman.py` | Contains pytest test cases for valid Roman numerals, subtractive notation, and invalid input. |
| `README.md`           | Documents the implementation, testing strategy, test categories, and learning outcomes.       |

---

## 3. Core Concepts & Exercise Breakdown

### 3.1 Roman Numeral Conversion Rules

Roman numerals use seven basic symbols.

| Symbol | Value |
| :----: | ----: |
|   `I`  |     1 |
|   `V`  |     5 |
|   `X`  |    10 |
|   `L`  |    50 |
|   `C`  |   100 |
|   `D`  |   500 |
|   `M`  |  1000 |

The implementation stores these values in a Python dictionary:

```python
roman = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}
```

This allows each Roman symbol to be looked up easily during conversion.

---

### 3.2 Additive and Subtractive Notation

Roman numerals normally use **additive notation**, where symbol values are added together.

Examples:

| Roman Numeral | Calculation | Result |
| :-----------: | :---------: | -----: |
|      `II`     |    1 + 1    |      2 |
|     `III`     |  1 + 1 + 1  |      3 |
|      `VI`     |    5 + 1    |      6 |
|     `XVI`     |  10 + 5 + 1 |     16 |

The implementation also supports **subtractive notation**.

Common subtractive combinations are:

| Combination | Meaning |
| :---------: | ------: |
|     `IV`    |       4 |
|     `IX`    |       9 |
|     `XL`    |      40 |
|     `XC`    |      90 |
|     `CD`    |     400 |
|     `CM`    |     900 |

The conversion logic compares the current symbol with the next symbol.

If the current value is smaller than the next value, the current value is subtracted.

For example:

```text
IX

I = 1
X = 10

1 < 10
Therefore: 10 - 1 = 9
```

For normal additive notation, the value is added.

```text
VI

V = 5
I = 1

5 is not smaller than 1
Therefore: 5 + 1 = 6
```

This comparison-based approach allows the same loop to handle both additive and subtractive notation.

---

### 3.3 Roman Numeral Validation

Simply calculating a numerical value is not enough to determine whether a Roman numeral is correctly written.

For example:

```text
IIII
VV
VX
XXC
```

may produce a numerical calculation, but they are not valid standard Roman numeral representations.

To solve this problem, the implementation uses `to_roman()` after calculating the integer value.

The logic is:

```text
Roman input
     ↓
Convert to integer
     ↓
Convert integer back to Roman numeral
     ↓
Compare with original input
     ↓
Same → Valid
Different → Invalid
```

For example:

```text
Input: XIX

convert("XIX")
      ↓
19
      ↓
to_roman(19)
      ↓
"XIX"
      ↓
Matches original input
      ↓
Valid
```

For an invalid input such as:

```text
IIII
```

the calculated value is `4`, but:

```text
to_roman(4)
```

returns:

```text
IV
```

Because:

```text
"IV" != "IIII"
```

the program raises a `ValueError`.

This provides an additional validation layer for Roman numeral formatting.

---

## 3.4 Test Categories

The test file divides the test cases into several categories based on different types of Roman numeral input.

| Category                     | Test Function                   | Example Input             | Expected Result |
| :--------------------------- | :------------------------------ | :------------------------ | :-------------- |
| Single symbol                | `test_single_symbol()`          | `I`, `V`                  | 1, 5            |
| Repeated symbols             | `test_repeated_symbols()`       | `II`, `III`               | 2, 3            |
| Different symbols            | `test_different_symbols()`      | `VI`, `XVI`               | 6, 16           |
| Subtractive notation         | `test_subtractive_notation()`   | `IV`, `IX`                | 4, 9            |
| Digit + subtractive notation | `test_digit_plus_subtractive()` | `XIX`                     | 19              |
| Invalid input                | `test_invalid_input()`          | `VX`, `IIII`, `ABC`, etc. | Exception       |

This categorization makes it easier to understand which part of the conversion logic each test is checking.

---

## 3.5 Equivalence Partitioning

**Equivalence Partitioning** divides input into groups where inputs are expected to behave similarly.

For this project, the main input categories are:

| Input Partition           | Example | Expected Behavior    |
| :------------------------ | :------ | :------------------- |
| Single valid symbol       | `I`     | Convert successfully |
| Repeated valid symbols    | `III`   | Convert successfully |
| Additive combination      | `VI`    | Convert successfully |
| Subtractive combination   | `IV`    | Convert successfully |
| Valid complex numeral     | `XIX`   | Convert successfully |
| Invalid Roman combination | `VX`    | Raise `ValueError`   |
| Invalid repetition        | `IIII`  | Raise `ValueError`   |
| Invalid characters        | `ABC`   | Raise `ValueError`   |
| Empty string              | `""`    | Raise `ValueError`   |
| Non-string input          | `123`   | Raise `TypeError`    |

Instead of testing every possible Roman numeral, representative examples are selected from different input categories.

---

## 3.6 Boundary and Edge Cases

The converter represents standard Roman numeral values from **1 to 3999**.

Important boundaries include:

| Boundary            | Example            | Purpose                                       |
| :------------------ | :----------------- | :-------------------------------------------- |
| Minimum value       | `I` → 1            | Tests the lowest valid Roman numeral          |
| Maximum value       | `MMMCMXCIX` → 3999 | Represents the highest standard Roman numeral |
| Empty input         | `""`               | Tests missing input                           |
| Invalid characters  | `ABC`              | Tests unsupported characters                  |
| Non-string input    | `123`              | Tests incorrect data type                     |
| Invalid repetition  | `IIII`, `VV`       | Tests Roman numeral formatting rules          |
| Invalid subtraction | `VX`, `XXC`        | Tests invalid subtractive combinations        |

The current test file focuses particularly on **logical edge cases and invalid input handling**, while the conversion implementation provides the underlying support for the standard range.

---

## 3.7 Defensive Validation

The `convert()` function performs validation before returning a result.

### Type Validation

The function first checks whether the input is a string:

```python
if not isinstance(number, str):
    raise TypeError("Input must be a string")
```

Therefore, an input such as:

```python
convert(123)
```

raises a `TypeError`.

### Empty Input Validation

After removing surrounding spaces and converting the input to uppercase, the function checks whether the input is empty:

```python
if not number:
    raise ValueError("Input cannot be empty")
```

Therefore:

```python
convert("")
```

raises a `ValueError`.

### Character Validation

Each character is checked against the supported Roman numeral symbols:

```python
for character in number:
    if character not in roman:
        raise ValueError(...)
```

Therefore:

```python
convert("ABC")
```

raises a `ValueError`.

This prevents unsupported characters from entering the conversion algorithm.

---

## 3.8 Exception Assertions with `pytest.raises`

Invalid inputs are tested using `pytest.raises()`.

Example:

```python
with pytest.raises(ValueError):
    convert("IIII")
```

This test does not expect a normal return value.

Instead, it verifies that the program correctly raises the expected exception.

The test suite checks several invalid cases:

```python
with pytest.raises(ValueError):
    convert("VX")

with pytest.raises(ValueError):
    convert("XXC")

with pytest.raises(ValueError):
    convert("IIII")

with pytest.raises(ValueError):
    convert("VV")

with pytest.raises(ValueError):
    convert("ABC")

with pytest.raises(ValueError):
    convert("")

with pytest.raises(TypeError):
    convert(123)
```

This demonstrates that automated testing should verify both:

1. **Correct results for valid input**
2. **Correct error handling for invalid input**

---

## 4. How to Run the Tests

The tests are written using the `pytest` framework.

From the project root directory, run:

```bash
pytest -v
```

### Meaning of `-v`

The `-v` option means **verbose mode**.

It displays the name and result of each test instead of only showing a short summary.

For example:

```text
tests/test_roman.py::test_single_symbol PASSED
tests/test_roman.py::test_repeated_symbols PASSED
```

This makes it easier to identify which individual test passed or failed.

### Run the Test File Directly

```bash
pytest tests/test_roman.py -v
```

### Run a Specific Test

For example:

```bash
pytest tests/test_roman.py::test_single_symbol -v
```

This is useful when debugging or checking one particular test category.

---

## 5. Testing Concepts Learned

### Test Assertions

The `assert` statement verifies that the actual result matches the expected result.

Example:

```python
assert convert("IV") == 4
```

This checks that the converter returns the expected integer value.

### Boundary and Edge Case Analysis

Testing should include values and inputs where errors are more likely to occur, such as:

* Minimum valid values
* Maximum valid values
* Empty input
* Invalid characters
* Invalid Roman numeral combinations
* Incorrect data types

### Equivalence Partitioning

Inputs can be divided into meaningful categories such as:

* Single symbols
* Repeated symbols
* Additive notation
* Subtractive notation
* Invalid characters
* Invalid Roman numeral structures

Representative inputs from each category can then be tested.

### Exception Testing

`pytest.raises()` verifies that invalid input produces the correct type of exception.

```python
with pytest.raises(ValueError):
    convert("ABC")
```

### Parameterization

The current test implementation uses grouped assertions rather than `pytest.mark.parametrize`.

For example, several related cases are currently tested inside:

```python
def test_invalid_input():
```

This keeps related invalid-input checks together and makes the testing categories easy to identify.

---

## 6. Expected Test Execution Summary

The current test file contains **6 test functions**:

1. `test_single_symbol`
2. `test_repeated_symbols`
3. `test_different_symbols`
4. `test_subtractive_notation`
5. `test_digit_plus_subtractive`
6. `test_invalid_input`

The invalid-input test contains multiple exception assertions, but pytest counts the entire function as **one test item**.

Therefore, the expected pytest result is:

```text
============================= test session starts =============================

collected 6 items

tests/test_roman.py::test_single_symbol PASSED
tests/test_roman.py::test_repeated_symbols PASSED
tests/test_roman.py::test_different_symbols PASSED
tests/test_roman.py::test_subtractive_notation PASSED
tests/test_roman.py::test_digit_plus_subtractive PASSED
tests/test_roman.py::test_invalid_input PASSED

============================== 6 passed in 0.XXs ===============================
```

The exact execution time may vary depending on the computer and Python environment.

A successful result of `6 passed` indicates that all six test functions completed successfully and that the expected valid conversions and exception conditions were satisfied.

---

## 7. Learning Outcomes

After completing this laboratory, the following learning outcomes were achieved:

1. **Understand Roman numeral conversion logic** by implementing additive and subtractive value calculations using symbol comparison.

2. **Apply unit testing principles** by creating separate test cases for different categories of input.

3. **Use assertions effectively** to compare actual conversion results with expected integer values.

4. **Test invalid and edge-case inputs** to verify that the program does not accept incorrectly formatted Roman numerals.

5. **Apply defensive validation and exception testing** using `TypeError`, `ValueError`, and `pytest.raises()`.

6. **Understand the importance of test coverage** by testing normal cases, boundary cases, invalid characters, invalid structures, empty input, and incorrect data types.

---

## Conclusion

This laboratory demonstrates the relationship between **implementation logic and automated testing**.

The Roman numeral converter first validates the input, converts each Roman symbol into its numerical value, handles additive and subtractive notation, and then validates the resulting Roman numeral format using the `to_roman()` function.

The test suite verifies these behaviors through different input categories, including valid symbols, repeated symbols, additive combinations, subtractive notation, and invalid input.

The main testing principle demonstrated in this laboratory is that a reliable test suite should not only verify that valid inputs produce correct results, but should also confirm that **invalid inputs are rejected with appropriate exceptions**.
