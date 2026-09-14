# Week 4: Assertion Testing

- **Course:** 192-211 Automated Software Testing
- **Lab:** Week 4 — Descriptive Testing
- **Exercise:** Assertion Testing
- **Files Used:**
  - `test_floats.py`
  - `test_collections.py` (also referred to as `test_collection.py`)

---

## 1. Exercise Title

**Week 4 — Automated Software Testing: Assertion Testing**

This lab exercise focuses on understanding, designing, and applying assertions in automated unit testing. By examining two test files—`test_floats.py` and `test_collections.py`—this module demonstrates how different data types (floating-point numbers, lists, dictionaries, and sets) require specific assertion strategies and comparison operations to verify expected program behavior reliably.

---

## 2. Purpose of Assertion Testing

In automated software testing, an **assertion** is a formal, executable statement that verifies whether a condition is true. It acts as an automated quality gate that confirms whether code behaves according to its design specification.

### The Core Assertion Mechanism

$$\textbf{Actual Result} \longrightarrow \textbf{Compare with Expected Result} \longrightarrow \textbf{Assertion Passes or Fails}$$

1. **Calculate or Retrieve Actual Result:** The code or expression under test executes, producing an actual value (e.g., `0.1 + 0.2` or `sorted(result)`).
2. **Define Expected Result:** The tester specifies the known correct outcome based on software requirements (e.g., `approx(0.3)` or `[1, 2, 3]`).
3. **Automate Comparison:** An `assert` statement evaluates whether the actual outcome matches the expected outcome.
   - If the expression evaluates to `True`, the assertion **passes**, and test execution continues.
   - If the expression evaluates to `False`, an `AssertionError` is raised, and the test **fails**.

### Why Assertions Are Critical
Without assertions, a test script merely runs code without checking whether the output is correct. A script that runs without crashing is not necessarily working correctly. Assertions provide **automated verification**, removing human guesswork and manual inspection from the testing process.

---

## 3. Testing Logic / Test Design

Assertions are not random statements sprinkled throughout a codebase; they are the final step in a deliberate testing thought process:

$$\textbf{What behavior do I want to verify?} \longrightarrow \textbf{What result should I expect?} \longrightarrow \textbf{What expression produces the actual result?} \longrightarrow \textbf{Which assertion is appropriate?}$$

### Example: Testing List Equality

Consider the test from `test_collections.py`:
```python
def test_list_equality():
    assert [1, 2, 3] == [1, 2, 3]
```

1. **What is being tested?**  
   We want to verify that two lists in Python are considered equal when they contain the exact same items in the exact same sequence.
2. **What is the expected result?**  
   The two lists `[1, 2, 3]` and `[1, 2, 3]` should evaluate as equivalent under Python's `==` comparison.
3. **Why is `==` appropriate?**  
   In Python, the `==` operator on sequences performs a deep, element-by-element equality check including index order. It is the direct and native way to verify list equivalence.
4. **What causes the test to pass?**  
   Both lists have length 3, and for every index $i$, `list1[i] == list2[i]`. The expression evaluates to `True`.
5. **What would cause the test to fail?**  
   Any difference in value (e.g., `[1, 2, 4]`), missing elements (e.g., `[1, 2]`), or differing element positions (e.g., `[1, 3, 2]`) would cause `==` to evaluate to `False`, failing the test.

---

## 4. `test_floats.py`

Floating-point numbers (numbers with decimal points, such as `0.1`, `0.2`, `0.3`) represent real numbers in computer hardware using the IEEE 754 standard. Because computer hardware stores data in binary (base-2) rather than decimal (base-10), certain base-10 fractions cannot be represented with infinite precision in a finite number of bits.

To handle floating-point comparisons safely in automated unit tests, `test_floats.py` imports pytest's built-in approximation helper:

```python
from pytest import approx
```

The `approx` helper wraps expected numerical values with a tolerance window, preventing tests from failing due to minuscule rounding artifacts.

---

## 5. Floating-Point Precision

The primary test in `test_floats.py` verifies floating-point addition:

```python
def test_float_precision():
    assert 0.1 + 0.2 == approx(0.3)
```

### Step-by-Step Analysis

1. **Calculation performed:**  
   The expression `0.1 + 0.2` adds two 64-bit IEEE 754 floating-point values in Python.
2. **Mathematically expected result:**  
   In base-10 arithmetic, $0.1 + 0.2 = 0.3$.
3. **Computer representation:**  
   In binary floating-point representation, numbers like `0.1` ($1/10$) and `0.2` ($1/5$) are repeating fractions (similar to $1/3 = 0.3333...$ in base-10). When Python calculates `0.1 + 0.2`, the binary rounding produces:
   $$\text{0.1 + 0.2} = \text{0.30000000000000004}$$
4. **What `approx()` does:**  
   The `approx(0.3)` helper creates an object that compares numbers within a relative tolerance (by default $1 \times 10^{-6}$). Instead of demanding absolute binary equality, it checks:
   $$| \text{actual} - \text{expected} | \le \text{tolerance}$$
5. **Why `approx(0.3)` is used instead of `== 0.3`:**  
   Comparing `0.1 + 0.2 == 0.3` directly in Python evaluates to `False` because `0.30000000000000004 != 0.3`. Using `approx(0.3)` accommodates machine rounding and checks that the value is close enough for practical correctness.
6. **What the assertion checks:**  
   It checks that `0.1 + 0.2` evaluates to a float sufficiently close to `0.3` within standard floating-point precision bounds.
7. **Why this is a useful test:**  
   It demonstrates how test authors must account for hardware-level floating-point limits rather than relying on naive equality.

---

## 6. Testing Without `approx()`

The second test in `test_floats.py` illustrates what happens when comparing floating-point expressions directly:

```python
def test_float_without_approx_fails():
    assert 0.1 + 0.2 != 0.3
```

### Explaining the Assertion
- **What this assertion tests:**  
  This assertion demonstrates the exact floating-point representation behavior of the machine: in Python, the expression `0.1 + 0.2` evaluates to `0.30000000000000004`. Because `0.30000000000000004` is numerically not identical to `0.30000000000000000`, the inequality check `!= 0.3` evaluates to `True`.
- **Important Distinction:**  
  This test does **not** claim that $0.1 + 0.2$ is mathematically different from $0.3$ in real-world mathematics. Rather, it demonstrates that standard binary floating-point arithmetic produces an IEEE 754 precision discrepancy that makes exact literal equality (`==`) unsafe for floating-point calculations.

### `== approx(0.3)` vs. `!= 0.3`

| Expression | Evaluates In Python As | Assertion Condition | Test Result | Purpose |
| :--- | :--- | :--- | :--- | :--- |
| `0.1 + 0.2 == approx(0.3)` | `0.30000000000000004 == approx(0.3)` | Evaluates to `True` within tolerance | **PASSED** | Practical verification of calculation |
| `0.1 + 0.2 != 0.3` | `0.30000000000000004 != 0.3` | Evaluates to `True` due to binary rounding | **PASSED** | Demonstrating binary representation artifact |

---

## 7. Collection Assertion Testing

The file `test_collections.py` demonstrates how to write assertions for three fundamental Python data structures:

1. **Lists (`list`):** Ordered, indexed, mutable sequences allowing duplicate items.
2. **Dictionaries (`dict`):** Key-value mappings where keys are unique and values are accessed by key.
3. **Sets (`set`):** Unordered collections of unique elements supporting mathematical set operations.

Each collection type requires a comparison strategy tailored to its internal data structure and semantics.

---

## 8. List Equality Test

```python
def test_list_equality():
    assert [1, 2, 3] == [1, 2, 3]
```

### Testing Logic
- **Two lists being compared:** The left-hand list `[1, 2, 3]` and right-hand list `[1, 2, 3]`.
- **Expected result:** Equality evaluates to `True`.
- **Why it passes:** In Python, two lists are equal (`listA == listB`) if and only if:
  1. They have the same number of elements (`len(listA) == len(listB)`).
  2. The elements at every corresponding index are equal (`listA[i] == listB[i]`).
- **What would cause failure:**  
  If any element differed (e.g., `[1, 2, 9]`) or if the order was swapped (e.g., `[3, 2, 1]`), the assertion would fail.
- **Key Takeaway:** List equality is **order-sensitive**.

---

## 9. List Contents Test

```python
def test_list_contents():
    result = [3, 1, 2]
    assert sorted(result) == [1, 2, 3]
```

### Testing Logic
- **The original list:** `result = [3, 1, 2]` contains elements `3`, `1`, and `2` in unsorted order.
- **Why not compare directly?**  
  Writing `assert [3, 1, 2] == [1, 2, 3]` would immediately fail because list equality enforces index-by-index ordering (`3 != 1`).
- **Why `sorted()` is used:**  
  The `sorted(result)` function creates a new sorted list: `[1, 2, 3]`. By sorting the list before asserting, the test normalizes the list into a canonical order.
- **What behavior the test verifies:**  
  The test verifies that `result` contains the exact set of elements `1`, `2`, and `3`, regardless of how they were ordered inside the initial collection.

---

## 10. Dictionary Equality Test

```python
def test_dict_equality():
    expected = {"name": "Alice", "age": 30}
    actual = {"age": 30, "name": "Alice"}
    assert actual == expected
```

### Testing Logic
- **`expected` represents:** The expected dictionary specification (`{"name": "Alice", "age": 30}`).
- **`actual` represents:** The dictionary produced by the program or system under test (`{"age": 30, "name": "Alice"}`).
- **Different key order:** In `expected`, `"name"` appears first. In `actual`, `"age"` appears first.
- **Why the assertion still passes:**  
  In Python, dictionary equality (`dictA == dictB`) compares **key-value pairs**, not key definition order. As long as every key in `expected` exists in `actual` with the identical corresponding value, `actual == expected` evaluates to `True`.
- **Testing Concept:** This demonstrates testing based on mapping equivalence rather than layout order.

---

## 11. Set Intersection Test

```python
def test_set_operations():
    assert {1, 2, 3} & {2, 3, 4} == {2, 3}
```

### Testing Logic
- **The `&` operator:** In Python sets, the `&` operator computes the **mathematical intersection** of two sets.
- **Intersection definition:** The set containing all elements that are members of *both* Set A and Set B.

### Step-by-Step Logic
```text
Set A            = {1, 2, 3}
Set B            = {2, 3, 4}

Common Elements  = {2, 3}
Expected Result  = {2, 3}
```

- **How the assertion verifies the operation:**  
  The expression `{1, 2, 3} & {2, 3, 4}` evaluates to `{2, 3}`. The assertion confirms that the resulting intersection matches `{2, 3}`.

---

## 12. Set Union Test

```python
def test_set_union_operations():
    assert {1, 2, 3, 4} | {3, 4, 5, 6, 7} == {1, 2, 3, 4, 5, 6, 7}
```

### Testing Logic
- **The `|` operator:** In Python sets, the `|` operator computes the **mathematical union** of two sets.
- **Union definition:** The set containing all distinct elements that appear in Set A, Set B, or both.
- **Handling duplicates:** Elements `3` and `4` exist in both sets. Because sets inherently enforce uniqueness, duplicates are automatically merged.

### Step-by-Step Logic
```text
Set A            = {1, 2, 3, 4}
Set B            = {3, 4, 5, 6, 7}

Combined Elements= {1, 2, 3, 4, 5, 6, 7}
Expected Result  = {1, 2, 3, 4, 5, 6, 7}
```

- **How the assertion verifies the operation:**  
  The expression `{1, 2, 3, 4} | {3, 4, 5, 6, 7}` evaluates to `{1, 2, 3, 4, 5, 6, 7}`. The assertion confirms that the resulting union correctly aggregates all unique elements.

---

## 13. Assertion Types Used

| Test Name | Assertion / Operation | Purpose | Data Type Verified |
| :--- | :--- | :--- | :--- |
| `test_float_precision` | `== approx(0.3)` | Compares floating-point values within an acceptable numerical tolerance | `float` |
| `test_float_without_approx_fails` | `!= 0.3` | Confirms that floating-point addition produces an IEEE 754 precision discrepancy | `float` |
| `test_list_equality` | `==` | Verifies element-by-element equivalence and order preservation | `list` |
| `test_list_contents` | `sorted()` + `==` | Normalizes sequence order to verify element presence | `list` |
| `test_dict_equality` | `==` | Verifies key-value mappings regardless of key insertion order | `dict` |
| `test_set_operations` | `&` + `==` | Verifies the mathematical intersection of two sets | `set` |
| `test_set_union_operations` | `\|` + `==` | Verifies the mathematical union of two sets, merging duplicates | `set` |

---

## 14. Expected Result and Test Logic Table

Below is the complete mapping of all 7 test functions defined across `test_floats.py` and `test_collections.py`:

| # | Test Function | File | Input / Expression | Expected Result | What the Assertion Verifies |
| :-: | :--- | :--- | :--- | :--- | :--- |
| 1 | `test_float_precision` | `test_floats.py` | `0.1 + 0.2 == approx(0.3)` | `True` | Verifies float addition matches expected value within pytest's default tolerance. |
| 2 | `test_float_without_approx_fails` | `test_floats.py` | `0.1 + 0.2 != 0.3` | `True` | Demonstrates IEEE 754 binary representation discrepancy (`0.30000000000000004 != 0.3`). |
| 3 | `test_list_equality` | `test_collections.py` | `[1, 2, 3] == [1, 2, 3]` | `True` | Verifies list equality requires identical items at identical indices. |
| 4 | `test_list_contents` | `test_collections.py` | `sorted([3, 1, 2]) == [1, 2, 3]` | `True` | Verifies list contents by normalizing order through sorting before comparison. |
| 5 | `test_dict_equality` | `test_collections.py` | `{"age": 30, "name": "Alice"} == {"name": "Alice", "age": 30}` | `True` | Verifies dictionary equality is based on matching key-value pairs regardless of key order. |
| 6 | `test_set_operations` | `test_collections.py` | `{1, 2, 3} & {2, 3, 4} == {2, 3}` | `True` | Verifies set intersection (`&`) returns common elements between two sets. |
| 7 | `test_set_union_operations` | `test_collections.py` | `{1, 2, 3, 4} \| {3, 4, 5, 6, 7} == {1, 2, 3, 4, 5, 6, 7}` | `True` | Verifies set union (`\|`) combines all unique elements from both sets. |

---

## 15. Why Assertions Make Tests Automated

In software testing, writing explicit assertions:

```python
assert actual == expected
```

transforms manual inspection into automated verification.

### Manual Inspection vs. Automated Pytest Assertions

| Manual Testing | Automated Assertion Testing |
| :--- | :--- |
| Developer prints output using `print()`. | Test writes `assert actual == expected`. |
| Human eyes must scan terminal output to spot errors. | Test runner (`pytest`) evaluates the condition automatically. |
| High chance of missing subtle discrepancies (e.g., float precision or swapped items). | Zero chance of human oversight: any mismatch triggers a failure. |
| Difficult to repeat across thousands of tests. | Can be run instantly and repeatedly in continuous integration (CI) pipelines. |

### How Pytest Handles Assertions
- **When True:** Execution silently succeeds, and the test is marked as **PASSED**.
- **When False:** An `AssertionError` is raised, and the test is marked as **FAILED**.
- **Assertion Introspection:** Pytest rewrites `assert` statements to display rich failure diagnostics, pinpointing the exact mismatched values, missing keys, or differing indices without extra boilerplate.

---

## 16. Test Independence

A cornerstone of sound unit testing is **test independence**. Every test function in `test_floats.py` and `test_collections.py` is completely isolated:

- Each test creates and computes its own local variables (e.g., `result = [3, 1, 2]`, `expected = {...}`, `actual = {...}`).
- There is **no shared global state**, no mutable class variables, and no dependency on test execution order.
- Any test can be run individually or in any sequence, and the outcome will always remain identical and deterministic.

---

## 17. How to Run the Tests

From your command terminal, navigate to the `Assertion_Testing` folder:

```bash
cd "Lab_03_descriptive_test_Week4/Assertion_Testing"
```

### 1. Run all tests with verbose output:
```bash
pytest -v
```

### 2. Run only the floating-point tests:
```bash
pytest test_floats.py -v
```

### 3. Run only the collection tests:
```bash
pytest test_collections.py -v
```

### Explanation of the `-v` Flag
The `-v` (verbose) flag instructs pytest to print the filename, individual test name, and completion status (`PASSED` or `FAILED`) for each test case instead of standard condensed progress dots (`.`).

---

## 18. Test Results

> Test execution results should be recorded after running pytest.

When executed in a Python environment with pytest installed:
- Pytest discovers all 7 test functions (2 in `test_floats.py` and 5 in `test_collections.py`).
- Each expression evaluates according to Python's data structure semantics and IEEE 754 floating-point rules.
- Each test runs in isolation, producing deterministic passing results when the implementations match the specifications.

---

## 19. Key Learning Outcomes

This lab exercise demonstrates the following core principles:

- **What Assertions Are:** Understanding assertions as automated verification gates that compare actual versus expected outcomes.
- **Automated Verification:** Replacing manual `print()` checks with repeatable pytest assertions.
- **Floating-Point Precision:** Recognizing IEEE 754 binary floating-point representation limits ($0.1 + 0.2 \ne 0.3$).
- **Using `pytest.approx()`:** Applying numerical tolerance to compare floating-point values reliably.
- **List Equality:** Verifying that list comparisons require matching elements and matching order.
- **Testing List Contents with Sorting:** Normalizing unordered sequences using `sorted()` to verify contents.
- **Dictionary Equality:** Confirming that dictionary comparison evaluates key-value pairs independently of key insertion order.
- **Set Intersection (`&`):** Verifying common element extraction between sets.
- **Set Union (`|`):** Verifying set combination and automated duplicate removal.
- **Appropriate Assertion Selection:** Choosing comparison techniques that align with data structure semantics.

---

## 20. Conclusion

Writing effective automated software tests requires more than simply executing code and typing `assert`. It requires an understanding of how data structures behave in memory and how different operations affect equality comparisons.

By selecting appropriate assertions—such as using `approx()` for floating-point numbers, `sorted()` for order-independent list verification, `==` for dictionary key-value mappings, and set operators for mathematical groups—test suites become accurate, robust, and capable of detecting genuine software defects.
