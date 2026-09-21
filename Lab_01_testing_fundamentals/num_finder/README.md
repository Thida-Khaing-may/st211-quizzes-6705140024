# NumFinder — Testing Fundamentals & Logic Bug Detection

## Course Information

| Item            | Information                                              |
| :-------------- | :------------------------------------------------------- |
| **Course**      | 192-211 Automated Software Testing                       |
| **Student**     | Thida Khaing                                             |
| **Student ID**  | 6705140024                                               |
| **Lab Topic**   | Testing Fundamentals, Unit Testing & Logic Bug Detection |
| **Institution** | Siam University                                          |

---

## 1. Overview

This laboratory introduces the motivation for automated software testing through a simple Python class called `NumFinder`.

The `NumFinder` class processes a list of numbers and identifies the **smallest** and **largest** values.

The laboratory demonstrates how automated tests can verify program behavior across different input patterns and help detect subtle logic errors.

The tests cover:

* Mixed-order numbers
* Descending lists
* Ascending lists
* A single-element list
* The difference between using two independent `if` statements and an `if`/`elif` structure

The descending-list test is particularly important because it demonstrates how a small change in control flow can cause incorrect results.

---

## 2. Project Structure

The project contains the following files:

```text
Lab_01_motivation/
│
├── README.md
│
└── num_finder/
    ├── num_finder.py
    └── test_num_finder.py
```

### File Description

| File                 | Purpose                                                                                       |
| :------------------- | :-------------------------------------------------------------------------------------------- |
| `num_finder.py`      | Contains the `NumFinder` class that finds the smallest and largest numbers.                   |
| `test_num_finder.py` | Contains automated tests for different number sequences and input conditions.                 |
| `README.md`          | Documents the purpose, testing approach, test cases, and learning outcomes of the laboratory. |

---

# 3. NumFinder Implementation

The `NumFinder` class stores two values:

```python
self.smallest = float('inf')
self.largest = float('-inf')
```

These initial values allow the algorithm to compare each number in the input list.

* `float('inf')` represents positive infinity.
* `float('-inf')` represents negative infinity.

Therefore, the first number processed can update both values when appropriate.

The main logic is:

```python
for n in nums:
    if n < self.smallest:
        self.smallest = n

    if n > self.largest:
        self.largest = n
```

Two separate `if` statements are used because a number may need to be evaluated for both conditions.

---

# 4. Test Cases

The test file contains four test cases. Each test focuses on a different input pattern.

## 4.1 Mixed Numbers

```python
def test_num_finder_mixed_numbers():
    # Arrange & Act
    nf = NumFinder()
    nf.find([4, 25, 7, 9])

    # Assert
    assert nf.largest == 25
    assert nf.smallest == 4
```

The input is:

```text
[4, 25, 7, 9]
```

The expected results are:

```text
Smallest = 4
Largest  = 25
```

This test checks the normal behavior of the algorithm using numbers that are not completely sorted.

### Testing Logic

The test creates a `NumFinder` object and passes the list to the `find()` method.

The final assertions verify that the algorithm correctly identifies both extremes.

---

## 4.2 Descending List — Detecting the `elif` Bug

```python
def test_num_finder_descending_list_catches_elif_bug():
    nf = NumFinder()
    nf.find([4, 3, 2, 1])

    assert nf.largest == 4
    assert nf.smallest == 1
```

The input is:

```text
[4, 3, 2, 1]
```

The expected results are:

```text
Smallest = 1
Largest  = 4
```

This is an important test because it can expose a control-flow problem if the implementation uses:

```python
if n < self.smallest:
    self.smallest = n
elif n > self.largest:
    self.largest = n
```

instead of:

```python
if n < self.smallest:
    self.smallest = n

if n > self.largest:
    self.largest = n
```

### Why Can `elif` Cause a Problem?

Consider the first value:

```text
n = 4
```

Initially:

```text
smallest = inf
largest  = -inf
```

The condition:

```text
4 < inf
```

is true, so `smallest` becomes `4`.

If `elif` is used, Python does not check the second condition for that same iteration.

Therefore:

```text
largest = -inf
```

can remain unchanged.

With two separate `if` statements, Python checks both conditions:

```text
4 < inf       → True  → smallest = 4
4 > -inf      → True  → largest = 4
```

This test therefore demonstrates why the two comparisons should be independent.

---

# 4.3 Ascending List

```python
def test_num_finder_ascending_list():
    nf = NumFinder()
    nf.find([1, 2, 3, 4])

    assert nf.largest == 4
    assert nf.smallest == 1
```

The input is:

```text
[1, 2, 3, 4]
```

The expected results are:

```text
Smallest = 1
Largest  = 4
```

This test verifies that the algorithm works correctly when the numbers are already arranged from smallest to largest.

---

# 4.4 Single-Element List

```python
def test_num_finder_single_element():
    nf = NumFinder()
    nf.find([5])

    assert nf.largest == 5
    assert nf.smallest == 5
```

The input contains only one value:

```text
[5]
```

Since there is only one number, it must be both the smallest and largest value.

Expected result:

```text
Smallest = 5
Largest  = 5
```

This is an important simple case because it checks how the algorithm behaves when the input contains no comparison between different numbers.

---

# 5. Test Case Summary

| Test                                               | Input           | Expected Smallest | Expected Largest | Purpose                                       |
| :------------------------------------------------- | :-------------- | :---------------: | :--------------: | :-------------------------------------------- |
| `test_num_finder_mixed_numbers`                    | `[4, 25, 7, 9]` |        `4`        |       `25`       | Tests normal mixed-order input.               |
| `test_num_finder_descending_list_catches_elif_bug` | `[4, 3, 2, 1]`  |        `1`        |        `4`       | Detects the possible `elif` control-flow bug. |
| `test_num_finder_ascending_list`                   | `[1, 2, 3, 4]`  |        `1`        |        `4`       | Tests an already sorted ascending sequence.   |
| `test_num_finder_single_element`                   | `[5]`           |        `5`        |        `5`       | Tests the single-element case.                |

---

# 6. Testing Concepts

## 6.1 Automated Testing

Instead of manually checking the output every time the program changes, automated tests allow the expected behavior to be checked repeatedly.

For example:

```python
assert nf.largest == 25
assert nf.smallest == 4
```

If the implementation changes and produces an incorrect result, pytest reports the corresponding test as failed.

---

## 6.2 Arrange, Act, Assert

The first test explicitly demonstrates the **Arrange-Act-Assert** structure.

```python
def test_num_finder_mixed_numbers():
    # Arrange & Act
    nf = NumFinder()
    nf.find([4, 25, 7, 9])

    # Assert
    assert nf.largest == 25
    assert nf.smallest == 4
```

The stages are:

| Stage       | Action                                            |
| :---------- | :------------------------------------------------ |
| **Arrange** | Create the `NumFinder` object.                    |
| **Act**     | Call `find()` with the test data.                 |
| **Assert**  | Check the calculated smallest and largest values. |

The Arrange and Act steps are combined in this particular test because the setup and method call are simple.

---

## 6.3 Testing Different Input Patterns

Testing only one input is not enough to provide confidence in an algorithm.

This lab uses several different patterns:

```text
Mixed:       [4, 25, 7, 9]
Descending:  [4, 3, 2, 1]
Ascending:   [1, 2, 3, 4]
Single:      [5]
```

Each pattern exercises the algorithm differently.

The descending sequence is especially useful because it checks the control flow that could be affected by replacing independent `if` statements with `elif`.

---

# 7. Why the `if` and `elif` Difference Matters

The implementation uses:

```python
if n < self.smallest:
    self.smallest = n

if n > self.largest:
    self.largest = n
```

These are two independent conditions.

This means Python evaluates both comparisons for every number.

In contrast:

```python
if n < self.smallest:
    self.smallest = n
elif n > self.largest:
    self.largest = n
```

means that the second condition is checked only when the first condition is false.

For this algorithm, that difference matters because the same number can satisfy both comparisons during the first iteration.

For example:

```text
Initial:
smallest = +infinity
largest  = -infinity

First number:
n = 4
```

With independent `if` statements:

```text
4 < +infinity  → True
smallest = 4

4 > -infinity  → True
largest = 4
```

Both values are correctly initialized.

This demonstrates how a small control-flow change can produce a logical error that may not be obvious from reading the code alone.

---

# 8. Running the Tests

Run the commands from the project directory.

## 8.1 Run All Tests

```bash
pytest
```

This allows pytest to automatically discover and execute the test functions.

---

## 8.2 Run Tests in Verbose Mode

```bash
pytest -v
```

The `-v` option displays the individual test names and their results.

A successful run should show the four NumFinder tests as passed.

The exact execution time may vary depending on the environment.

---

## 8.3 Run Only the NumFinder Tests

If the test file is inside the `num_finder` directory, use:

```bash
pytest num_finder/test_num_finder.py -v
```

This runs only the tests related to `NumFinder`.

---

## 8.4 Run One Specific Test

For example:

```bash
pytest num_finder/test_num_finder.py::test_num_finder_descending_list_catches_elif_bug -v
```

This is useful when investigating the behavior of the descending-list case.

---

# 9. Expected Test Result

When the current implementation is used, the four provided tests should pass:

```text
test_num_finder_mixed_numbers PASSED
test_num_finder_descending_list_catches_elif_bug PASSED
test_num_finder_ascending_list PASSED
test_num_finder_single_element PASSED
```

The expected result is:

```text
4 passed
```

The exact output formatting and execution time may vary depending on the pytest version and environment.

---

# 10. Learning Outcomes

After completing this laboratory, I can:

1. **Write basic automated unit tests** using Python and `pytest`.

2. **Use assertions** to compare actual results with expected results.

3. **Test different input patterns** instead of relying on only one normal example.

4. **Apply the Arrange-Act-Assert pattern** to organize test logic.

5. **Identify control-flow bugs** caused by using `elif` when independent conditions are required.

6. **Understand the value of automated testing** for detecting errors that may not be obvious during manual inspection.

7. **Run individual tests and complete test suites** using pytest commands.

---

# 11. Conclusion

The `NumFinder` example demonstrates why automated testing is useful even for a small program.

The tests do more than verify that the algorithm works with one normal input. They check different number arrangements and a single-element case, while the descending-list test specifically helps detect a potential `if`/`elif` logic error.

This laboratory shows that carefully selected test cases can reveal problems in program logic and provide confidence that the implementation behaves correctly across different input conditions.
