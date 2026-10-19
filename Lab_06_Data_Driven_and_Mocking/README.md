# Lab 06: Data-Driven Testing and Mocking

## Course Information

| Item | Information |
| :--- | :--- |
| **Course** | 192-211 Automated Software Testing |
| **Student** | Thida Khaing |
| **Student ID** | 6705140024 |
| **Lab** | Lab 06 — Data-Driven Testing and Mocking |

---

## Overview

This lab demonstrates how to use **parameterized fixtures, data-driven testing, and mocking in Pytest**. These techniques help test different configurations, reuse external test data, and control dependencies during automated testing.

The lab covers parameterized fixtures for browser and database configurations, loading test cases from JSON and CSV files, validating login inputs, and using `unittest.mock.patch` to test different weather conditions without depending on randomly generated temperatures.

## Directory Structure

```text
Lab_06_Data_Driven_and_Mocking/
├── test_param_fixture.py
├── test_browsers.py
├── test_cases.json
├── test_data_driven.py
├── load_data/
│   ├── logins.csv
│   ├── validate.py
│   └── test_csv_driven.py
├── weather/
│   ├── weather.py
│   ├── test_problems.py
│   └── test_solutions.py
└── README.md
```

## Modules and Test Specifications

### 1. Parameterized Fixtures

**Files:** `test_param_fixture.py`, `test_browsers.py`

- **`test_param_fixture.py`**: Demonstrates the use of `pytest.fixture(params=...)` to provide different parameter values to tests. The lab includes browser and database configurations.
- **`test_browsers.py`**: Uses a parameterized browser fixture to test page loading and button clickability with Chrome, Firefox, and Safari.
- The browser fixture uses `yield` to separate setup and teardown operations. It prints a message when launching a browser and another message when closing it.

Parameterized fixtures allow the same test function to run with multiple configurations, reducing repetitive code.

### 2. JSON-Driven Testing

**Files:** `test_cases.json`, `test_data_driven.py`

- **`test_cases.json`**: Stores input strings and their expected uppercase results as JSON data.
- **`test_data_driven.py`**: Uses the `json` module to read the test cases from the JSON file.
- The `load_cases()` function extracts each input and its expected result.
- `@pytest.mark.parametrize` generates individual test cases from the loaded data.
- The tests verify uppercase conversion for `hello`, `world`, `PyTest`, and `123abc`.

This approach separates test data from test logic, making it easier to add or modify test cases without creating a separate test function for every input.

### 3. CSV-Driven Login Testing

**Files:** `load_data/logins.csv`, `load_data/validate.py`, `load_data/test_csv_driven.py`

- **`logins.csv`**: Stores usernames, passwords, and expected login-validation results.
- **`validate.py`**: Defines the `is_valid_login(username, password)` function.
- **`test_csv_driven.py`**: Uses Python's `csv` module and `csv.DictReader` to load login test cases from the CSV file.
- The loader converts the expected result from a string into a Boolean value.
- `@pytest.mark.parametrize` runs the login-validation test for each CSV record.

The test data includes valid credentials and invalid cases with an empty username or password. The expected results are compared with the actual output of `is_valid_login()`.

This technique makes it possible to test many input combinations by updating the CSV file rather than changing the test function.

### 4. Testing Random Behavior with Mocking

**Files:** `weather/weather.py`, `weather/test_problems.py`, `weather/test_solutions.py`

- **`weather.py`**: Defines `get_temperature()`, which returns a random temperature between -10 and 40, and `describe_weather()`, which classifies the temperature.
- **`test_problems.py`**: Checks whether the returned weather description belongs to the expected set of descriptions.
- **`test_solutions.py`**: Uses `unittest.mock.patch` to replace `weather.get_temperature()` with a controlled return value for each test.

The weather descriptions are determined by the following conditions:

| Temperature | Expected description |
| :--- | :--- |
| Below 0°C | Freezing |
| 0°C to below 15°C | Cold |
| 15°C to below 25°C | Pleasant |
| 25°C to 40°C | Hot |

The solution tests provide fixed temperatures to check each condition. For example, a temperature of -5°C should return `Freezing`, while 30°C should return `Hot`.

Mocking makes the tests more predictable because they do not depend on the random temperature generated during execution.

## How to Run the Tests

Run the commands from the `Lab_06_Data_Driven_and_Mocking` directory unless a command specifies a subdirectory.

**Run the browser tests:**

```bash
pytest test_browsers.py -v -s
```

**Run the parameterized fixture tests:**

```bash
pytest test_param_fixture.py -v -s
```

**Run the JSON-driven tests:**

```bash
pytest test_data_driven.py -v
```

**Run the CSV-driven tests:**

```bash
cd load_data
pytest test_csv_driven.py -v
```

**Run the weather tests:**

```bash
cd ../weather
pytest test_problems.py -v
pytest test_solutions.py -v
```

**Run the complete lab test suite:**

```bash
cd ..
pytest -v -s
```

The `-v` option displays detailed test names and results. The `-s` option displays printed output from the tests, including the browser setup and teardown messages.

The complete suite should be run from the lab root directory after checking that the CSV and JSON data files can be located correctly.

## Verified Test Summary

The following table summarizes the individual test runs recorded during this lab.

| Test File | Recorded cases | Passed | Failed |
| :--- | ---: | ---: | ---: |
| `test_param_fixture.py` | 3 | 3 | 0 |
| `test_browsers.py` | 6 | 6 | 0 |
| `test_data_driven.py` | 4 | 4 | 0 |
| `load_data/test_csv_driven.py` | 4 | 4 | 0 |
| `weather/test_problems.py` | 1 | 1 | 0 |
| `weather/test_solutions.py` | 4 | 4 | 0 |
| **Total recorded individual runs** | **22** | **22** | **0** |

**Important:** These figures summarize the recorded individual test runs. They do not establish that the entire lab passed in one complete execution. The recorded logs include earlier collection errors related to imports and locating `logins.csv`. The full suite should be rerun successfully from the lab root before claiming that all tests pass together.

## Key Learning Outcomes

After completing this lab, I learned how to:

- Use parameterized fixtures to test multiple configurations.
- Apply setup and teardown operations using a fixture with `yield`.
- Load external test data from JSON and CSV files.
- Use `@pytest.mark.parametrize` to generate tests from external data.
- Validate login inputs using data-driven test cases.
- Use `unittest.mock.patch` to control dependencies during testing.
- Test different branches of a function using fixed inputs.
- Interpret Pytest results and troubleshoot import and file-path errors.

## Conclusion

This lab helped me understand how data-driven testing and mocking improve automated testing. Parameterized fixtures allow the same tests to run with different configurations, while JSON and CSV files make test data easier to maintain. Mocking also allows tests to check specific conditions without depending on unpredictable external behavior, such as randomly generated temperatures.

These techniques make test suites more reusable, predictable, and easier to maintain.
