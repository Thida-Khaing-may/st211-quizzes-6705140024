# Lab — Skipping Tests and Expected Failures

**Course:** 192-211 Automated Software Testing
**Student:** Thida Khaing
**Student ID:** 6705140024

## Overview

This lab demonstrates how `pytest` handles tests that should **not be executed normally**.

In real software projects, some tests may need to be skipped because a feature is not ready, a required environment condition is not available, or a test is temporarily not applicable. Other tests may currently fail because a known bug has not been fixed yet.

This lab covers two important pytest features:

* **Skipping tests** using `skip` and `skipif`
* **Expected failures** using `xfail`

The examples also demonstrate how `pytest.ini` can be used to configure test discovery, command-line options, and custom markers.

---

## Learning Objectives

After completing this lab, I can:

* Understand why a test may need to be skipped.
* Use `@pytest.mark.skip` to always skip a test.
* Use `@pytest.mark.skipif()` to skip a test only when a condition is true.
* Use `sys.version_info` to check the Python version.
* Use `os.path.exists()` to check whether a file exists.
* Understand the difference between **SKIPPED** and **XFAIL**.
* Use `@pytest.mark.xfail` for tests that are expected to fail.
* Configure pytest markers in `pytest.ini`.
* Run and interpret skipped, passed, failed, and expected-failure test results.

---

## Project Structure

```text
Skipping_and_Xfail/
│
├── pytest.ini
├── README.md
├── test_conditionals.py
├── test_skips.py
└── test_xfail.py
```

### File Description

| File                   | Purpose                                        |
| ---------------------- | ---------------------------------------------- |
| `pytest.ini`           | Configures pytest and registers custom markers |
| `README.md`            | Documents the lab and explains the concepts    |
| `test_conditionals.py` | Demonstrates condition-based test execution    |
| `test_skips.py`        | Demonstrates `skip` and `skipif`               |
| `test_xfail.py`        | Demonstrates expected failures using `xfail`   |

---

# 1. Pytest Configuration

The `pytest.ini` file contains the configuration used by this lab.

```ini
[pytest]

testpaths = .

addopts = -v --tb=short --strict-markers

markers =
    smoke: critical path tests
    slow: tests that take a long time
    regression: tests for previously fixed bugs

python_files = test_*.py
python_classes = Test*
python_functions = test_*
```

### Configuration Explanation

#### `testpaths = .`

Tells pytest to search for tests starting from the current directory.

#### `addopts = -v --tb=short --strict-markers`

These options are automatically applied whenever pytest runs.

* `-v` — displays detailed test results.
* `--tb=short` — shows shorter traceback information when a test fails.
* `--strict-markers` — reports an error if an unregistered marker is used.

#### `markers`

Registers custom markers that can be used to categorize tests.

For example:

```python
@pytest.mark.smoke
def test_login():
    ...
```

The markers in this configuration are:

* `smoke` — critical-path tests
* `slow` — tests that take a long time
* `regression` — tests for previously fixed bugs

#### Test discovery settings

```ini
python_files = test_*.py
python_classes = Test*
python_functions = test_*
```

These tell pytest which files, classes, and functions should be recognized as tests.

---

# 2. Skipping Tests

A skipped test is a test that pytest **does not execute**.

Skipping can be useful when:

* A feature has not been implemented yet.
* A test only works in a particular environment.
* A required operating-system feature is unavailable.
* A test temporarily cannot be executed.

There are two main ways demonstrated in this lab:

```python
@pytest.mark.skip
```

and

```python
@pytest.mark.skipif(...)
```

---

## 2.1 Unconditionally Skipping a Test

Example from `test_skips.py`:

```python
@pytest.mark.skip(reason="Feature not implemented yet")
def test_future_feature():
    assert False
```

`@pytest.mark.skip` tells pytest to skip the test every time.

Although:

```python
assert False
```

would normally cause a test failure, pytest does not execute the test because it has been marked as skipped.

The result is similar to:

```text
SKIPPED
```

### When to use it

This is useful when a test is written for a feature that is **not available yet**.

For example:

```text
Feature not implemented
        ↓
Test cannot be used yet
        ↓
Mark the test as skipped
```

---

# 3. Conditional Skipping with `skipif`

`skipif` skips a test only when a specified condition is `True`.

Example:

```python
@pytest.mark.skipif(
    sys.version_info < (3, 8),
    reason="Requires Python 3.8+"
)
def test_needs_modern_python():
    assert True
```

The condition is:

```python
sys.version_info < (3, 8)
```

This means:

> Skip the test if the current Python version is lower than Python 3.8.

### Example

| Python version | Result  |
| -------------- | ------- |
| Python 3.7     | SKIPPED |
| Python 3.8     | PASSED  |
| Python 3.10    | PASSED  |
| Python 3.14    | PASSED  |

This allows a test to run only in an environment that supports the required Python version.

---

# 4. Checking Operating-System Conditions

Another example uses:

```python
os.path.exists("/etc/hosts")
```

Example:

```python
@pytest.mark.skipif(
    not os.path.exists("/etc/hosts"),
    reason="No hosts file"
)
def test_hosts_file():
    assert os.path.exists("/etc/hosts")
```

The test first checks whether `/etc/hosts` exists.

If the file does not exist:

```python
not os.path.exists("/etc/hosts")
```

becomes `True`, so pytest skips the test.

If the file exists, the test runs.

### Important note for Windows

The path:

```text
/etc/hosts
```

is commonly used on Linux and macOS.

On Windows, the hosts file is normally located at:

```text
C:\Windows\System32\drivers\etc\hosts
```

Therefore, when running this example on Windows, the test may be skipped because `/etc/hosts` does not exist.

This is an example of why conditional skipping can be useful when tests depend on the operating system.

---

# 5. Expected Failures with `xfail`

`xfail` is different from `skip`.

```python
@pytest.mark.xfail(reason="Known bug #123, fix pending")
def test_known_broken_feature():
    assert 1 == 2
```

This test is **expected to fail**.

Normally:

```python
assert 1 == 2
```

would produce:

```text
FAILED
```

But because the test is marked with:

```python
@pytest.mark.xfail
```

pytest understands that the failure is expected.

The result is reported as:

```text
XFAIL
```

### Why use `xfail`?

It is useful when:

* A known bug exists.
* The test describes the correct behavior.
* The bug has not been fixed yet.
* The team wants to keep the test without treating the known failure as a normal unexpected failure.

---

# 6. When an XFail Test Actually Passes

Consider this test:

```python
@pytest.mark.xfail(reason="Might pass sometimes")
def test_actually_works_now():
    assert 1 == 1
```

The test is marked as expected to fail, but the assertion actually passes.

In this situation, pytest reports:

```text
XPASS
```

which means:

> Expected Failure, but the test unexpectedly passed.

This can be useful because it may indicate that a previously broken feature has started working.

The developer can then investigate the test and decide whether the `xfail` marker should be removed.

---

# 7. `skip` vs `skipif` vs `xfail`

| Feature  | Test runs?           | Expected result            | Main purpose                         |
| -------- | -------------------- | -------------------------- | ------------------------------------ |
| `skip`   | No                   | `SKIPPED`                  | Always skip the test                 |
| `skipif` | Depends on condition | `SKIPPED` or normal result | Skip only in specific situations     |
| `xfail`  | Yes                  | Failure is expected        | Document a known or expected failure |

### Simple way to remember

```text
skip
↓
"Don't run this test."

skipif
↓
"Don't run this test if this condition is true."

xfail
↓
"Run this test, but we expect it to fail."
```

---

# 8. Test Results

When running the tests, pytest may report several different outcomes.

| Result    | Meaning                                          |
| --------- | ------------------------------------------------ |
| `PASSED`  | The test ran and passed                          |
| `FAILED`  | The test ran and failed unexpectedly             |
| `SKIPPED` | The test was intentionally not executed          |
| `XFAIL`   | The test failed as expected                      |
| `XPASS`   | The test passed even though failure was expected |

Understanding these results is important when reading a pytest test report.

---

# 9. Running the Tests

Open a terminal inside the `Skipping_and_Xfail` directory.

Run all tests:

```bash
pytest
```

Because `pytest.ini` contains:

```ini
addopts = -v --tb=short --strict-markers
```

pytest automatically uses those options.

You can also run a specific file:

```bash
pytest test_skips.py
```

```bash
pytest test_xfail.py
```

```bash
pytest test_conditionals.py
```

---

# 10. Expected Behavior

The tests in this lab are designed to demonstrate different pytest outcomes.

For example:

```text
test_future_feature       SKIPPED
test_needs_modern_python  PASSED
test_hosts_file           SKIPPED/PASSED
test_known_broken_feature XFAIL
test_actually_works_now   XPASS
```

The exact result of `test_hosts_file` depends on the operating system.

The exact result of conditional tests can also depend on the Python version and environment where the tests are executed.

---

# 11. Key Takeaways

This lab demonstrates that not every test should always be treated as a normal pass/fail test.

### `skip`

Use when the test should not run at all.

```python
@pytest.mark.skip(reason="...")
```

### `skipif`

Use when the test should only be skipped under a particular condition.

```python
@pytest.mark.skipif(condition, reason="...")
```

### `xfail`

Use when the test should run but a failure is currently expected.

```python
@pytest.mark.xfail(reason="...")
```

These features help test suites handle unfinished features, environment differences, known bugs, and changing software behavior without losing useful tests.

---

## Lab Summary

In this lab, I practiced:

* Configuring pytest with `pytest.ini`
* Registering custom markers
* Skipping tests with `skip`
* Conditionally skipping tests with `skipif`
* Checking Python version information with `sys.version_info`
* Checking file availability with `os.path.exists()`
* Marking known failures with `xfail`
* Understanding `XFAIL` and `XPASS`
* Interpreting pytest test results
* Running tests from the command line

The main difference is:

> **Skip means the test is not executed, while xfail means the test is executed but its failure is expected.**
