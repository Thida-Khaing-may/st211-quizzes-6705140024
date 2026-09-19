# Lab 01 — Why Do We Test Software? (A Motivating Example)

## Course Information

- **Course:** 192-211 Automated Software Testing
- **Student:** Thida Khaing 
- **Student ID:** 6705140024
- **Lab:01** Week 1 — Software Testing Motivation & Edge Cases

## 1. Overview

The purpose of this laboratory is to understand why systematic software testing is necessary, even for short, seemingly straightforward programs.

A program can pass an initial manual test and still contain logical flaws when presented with different input orders or edge cases. This lab uses a numeric scanner (`NumFinder`) to demonstrate:

* How subtle branching logic bugs, such as an incorrect `elif`, can occur.
* How automated test cases expose edge case failures systematically.
* How to write independent, automated unit tests using Python and `pytest`.

---

## 2. Project Structure

The project contains the following files:

```text
Lab_01_motivation/
│
├── README.md
├── num_finder.py
└── test_num_finder.py
```

### File Description

| File                 | Purpose                                                                                             |
| :------------------- | :-------------------------------------------------------------------------------------------------- |
| `num_finder.py`      | Implements the `NumFinder` class to track the smallest and largest values in a collection.          |
| `test_num_finder.py` | Contains automated test cases verifying standard lists, sorted orderings, and regression scenarios. |

---

## 3. Core Concepts & Implementation Breakdown

### 3.1 The Problem: The `elif` Branch Trap

The initial implementation of `NumFinder` attempted to track values using an `if / elif` structure:

```python
# Flawed implementation
class NumFinder:
    def __init__(self):
        self.smallest = float('inf')
        self.largest = float('-inf')

    def find(self, nums):
        for n in nums:
            if n < self.smallest:
                self.smallest = n
            elif n > self.largest:
                self.largest = n
```

When tested with a mixed list like `[4, 25, 7, 9]`, the code produced:

* `smallest = 4`
* `largest = 25`

This creates a false sense of security.

However, when passed a **strictly descending list** like `[4, 3, 2, 1]`, every successive number is smaller than the previous smallest:

1. `4 < inf` → `smallest = 4` (`elif` is skipped)
2. `3 < 4` → `smallest = 3` (`elif` is skipped)
3. `2 < 3` → `smallest = 2` (`elif` is skipped)
4. `1 < 2` → `smallest = 1` (`elif` is skipped)

Because the `elif` branch is skipped on every iteration, `self.largest` is never updated and remains at its initial value of `-inf`.

### 3.2 The Solution: Independent Branch Conditions

To fix the defect, the two tracking conditions must evaluate independently on every number. Replacing `elif` with an independent `if` statement ensures that an element can be evaluated against both minimum and maximum thresholds:

```python
# Corrected implementation
class NumFinder:
    def __init__(self):
        self.smallest = float('inf')
        self.largest = float('-inf')

    def find(self, nums):
        for n in nums:
            if n < self.smallest:
                self.smallest = n
            if n > self.largest:
                self.largest = n
```

---

## 4. Test Suite Breakdown

The test suite in `test_num_finder.py` applies the **AAA pattern (Arrange, Act, Assert)** to verify normal behavior, edge cases, and regression resistance.

### 4.1 Test Case Matrix

| Test Function                                      | Input Data      | Target Behavior                                      | Expected Outcome               |
| :------------------------------------------------- | :-------------- | :--------------------------------------------------- | :----------------------------- |
| `test_num_finder_mixed_numbers`                    | `[4, 25, 7, 9]` | Standard unordered list                              | `smallest = 4`, `largest = 25` |
| `test_num_finder_descending_list_catches_elif_bug` | `[4, 3, 2, 1]`  | Descending ordered list that catches the `elif` flaw | `smallest = 1`, `largest = 4`  |
| `test_num_finder_ascending_list`                   | `[1, 2, 3, 4]`  | Ascending ordered list                               | `smallest = 1`, `largest = 4`  |
| `test_num_finder_single_element`                   | `[5]`           | Single-item boundary case                            | `smallest = 5`, `largest = 5`  |

### 4.2 My Testing Logic

* **`test_num_finder_descending_list_catches_elif_bug`**: This is a critical regression test. It directly targets the control-flow flaw where every value updates `smallest`, ensuring `largest` is still evaluated correctly.
* **`test_num_finder_single_element`**: This represents a boundary condition. A single value must simultaneously be both the smallest and the largest number in the collection.
* **AAA Separation**: Each test sets up a fresh `NumFinder()` instance (Arrange), calls `.find()` (Act), and asserts the properties (Assert), ensuring tests remain isolated and independent.

---

## 5. How to Run the Tests

Run the following commands from the project directory.

### Run All Tests

```bash
pytest -v
```

The `-v` (verbose) flag displays each test method and its execution status.

### Run an Individual Test

To target the regression test specifically:

```bash
pytest test_num_finder.py::test_num_finder_descending_list_catches_elif_bug -v
```

---

## 6. Expected Test Execution Summary

When all tests pass, the output displays:

```text
============================= test session starts =============================
collected 4 items

test_num_finder.py::test_num_finder_mixed_numbers PASSED                 [ 25%]
test_num_finder.py::test_num_finder_descending_list_catches_elif_bug PASSED [ 50%]
test_num_finder.py::test_num_finder_ascending_list PASSED               [ 75%]
test_num_finder.py::test_num_finder_single_element PASSED              [100%]

============================== 4 passed in 0.02s ==============================
```

---

## 7. Learning Outcomes

1. **The Risk of Incomplete Verification**: A program passing one arbitrary input does not prove it is correct under other valid sequences.
2. **Order Dependency as an Edge Case**: The order of input items, such as a strictly descending order, can cause conditional branches to fail silently.
3. **Automated Regression Prevention**: Writing unit tests ensures that once a bug is fixed, future updates will not reintroduce the same defect.
