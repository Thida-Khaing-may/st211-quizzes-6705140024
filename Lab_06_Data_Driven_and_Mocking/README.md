# Lab 06: Data-Driven Testing and Mocking Dependencies

## Course Information

| Item | Information |
| :--- | :--- |
| **Course** | 192-211 Automated Software Testing |
| **Student** | Thida Khaing |
| **Student ID** | 6705140024 |
| **Lab** | Lab 06 — Data-Driven Testing and Mocking Dependencies |

---

## Overview

This lab explores different techniques for improving automated testing with Python and Pytest. It covers parameterized fixtures, data-driven testing using JSON and CSV files, and mocking external dependencies to make tests more controlled and predictable.

The lab also introduces the `unittest.mock` library, including `Mock`, `patch`, `return_value`, and `side_effect`. These techniques allow tests to replace real dependencies, simulate different responses, verify function calls, and test application behavior without relying on external systems.

## Directory Structure

```text
Lab_06_Data_Driven_and_Mocking/
├── README.md
├── test_param_fixture.py
├── test_browsers.py
├── test_cases.json
├── test_data_driven.py
│
├── Exercise/
│   ├── test_mock_basics.py
│   ├── test_return_value.py
│   ├── test_side_effect_exception.py
│   ├── test_side_effect_list.py
│   ├── test_side_effect_function.py
│   └── test_comparison.py
│
├── load_data/
│   ├── logins.csv
│   ├── validate.py
│   └── test_csv_driven.py
│
├── Patching_Dependencies/
│   ├── date_utils.py
│   ├── notifications.py
│   ├── test_date_utils.py
│   └── test_notifications.py
│
├── Return_Value_and_Dependency_Injection/
│   ├── payment.py
│   ├── return_value.py
│   ├── test_payment.py
│   ├── test_return_values.py
│   └── test_user_service.py
│
├── Verifying_Calls/
│   └── test_verify_calls.py
│
├── weather/
│   ├── weather.py
│   ├── test_problems.py
│   └── test_solutions.py
│
└── Weather_Decorator/
    └── test_weather_decorator.py
```

*Note: The structure above follows the folder and file names provided. Add any other files that exist in your actual directory.*

## Modules and Test Specifications

### 1. Parameterized Fixtures

**Files:** `test_param_fixture.py`, `test_browsers.py`

- **`test_param_fixture.py`**: Uses `@pytest.fixture(params=[...])` to run the same test with different database configurations: SQLite, PostgreSQL, and MySQL.
- **`test_browsers.py`**: Uses a parameterized fixture to test different browser names: Chrome, Firefox, and Safari.
- Demonstrates how `request.param` provides the current parameter to a fixture.
- Uses `yield` to separate fixture setup and teardown operations.

The parameterized fixture helps reuse the same test logic across multiple configurations without writing separate test functions.

### 2. JSON-Driven Testing

**Files:** `test_cases.json`, `test_data_driven.py`

- **`test_cases.json`**: Stores input strings and their expected uppercase results.
- **`test_data_driven.py`**: Uses Python's `json` module to load test cases from the JSON file.
- Uses `@pytest.mark.parametrize` to execute the test function with each input and expected result.
- Tests strings such as `"hello"`, `"world"`, `"PyTest"`, and `"123abc"`.

This approach separates test data from test logic, making it easier to add or modify test cases without changing the test function.

### 3. CSV-Driven Testing

**Files:** `load_data/logins.csv`, `load_data/validate.py`, `load_data/test_csv_driven.py`

- **`logins.csv`**: Contains username, password, and expected login-validation results.
- **`validate.py`**: Defines the `is_valid_login(username, password)` function, which checks that both fields are present and are not empty or whitespace-only.
- **`test_csv_driven.py`**: Uses Python's `csv` module to read test cases from the CSV file.
- Converts the expected result from the CSV text into a Boolean value.
- Uses `@pytest.mark.parametrize` to test each row of data.

The CSV file includes valid and invalid login cases, such as empty usernames and missing passwords.

This exercise demonstrates how external CSV data can be used to test different input combinations efficiently.

### 4. Basic Mock Objects and Mock Behavior Comparison

**Files:** `Exercise/test_mock_basics.py`, `Exercise/test_return_value.py`, `Exercise/test_side_effect_exception.py`, `Exercise/test_side_effect_list.py`, `Exercise/test_side_effect_function.py`, `Exercise/test_comparison.py`

- **`test_mock_basics.py`**: Creates mock objects using `unittest.mock.Mock`. Tests dynamically created methods and calls with arguments.
- **`test_return_value.py`**: Uses `return_value` to configure fixed string and integer responses.
- **`test_side_effect_exception.py`**: Uses `side_effect` to simulate `ValueError` and `RuntimeError`, verifying the exceptions with `pytest.raises()`.
- **`test_side_effect_list.py`**: Uses a list as `side_effect` to return sequential values. Also checks that an exhausted iterable raises `StopIteration`.
- **`test_side_effect_function.py`**: Assigns a custom function to `side_effect` to perform calculations using arguments passed to the mock.
- **`test_comparison.py`**: Compares static return values, sequential responses, exception handling, and callable side effects.

The exercises demonstrate the differences between `return_value` and `side_effect`:

| Mock configuration | Behavior |
| :--- | :--- |
| `return_value` | Returns the same configured value on repeated calls. |
| `side_effect` with an exception | Raises the configured exception when called. |
| `side_effect` with a list | Returns the next item on each call. |
| `side_effect` with a function | Executes custom logic using the supplied arguments. |

### 5. Patching Dependencies

**Files:** `Patching_Dependencies/date_utils.py`, `Patching_Dependencies/notifications.py`, `Patching_Dependencies/test_date_utils.py`, `Patching_Dependencies/test_notifications.py`

- **`date_utils.py`**: Contains `get_year()` and `report_name()`. The report name uses the year returned by `get_year()`.
- **`test_date_utils.py`**: Uses `unittest.mock.patch` to replace `date_utils.get_year()` with a controlled return value of `2030`. It verifies that the report name becomes `"Report-2030"`.
- **`notifications.py`**: Contains `send_email()` and `notify_user()`. The notification function calls the email-sending dependency.
- **`test_notifications.py`**: Patches `notifications.send_email` so the test can verify the notification result without sending a real email.

Patching allows a test to temporarily replace a dependency with a mock object. This helps prevent tests from depending on real external services.

### 6. Return Values and Dependency Injection

**Files:** `Return_Value_and_Dependency_Injection/payment.py`, `Return_Value_and_Dependency_Injection/return_value.py`, `Return_Value_and_Dependency_Injection/test_payment.py`, `Return_Value_and_Dependency_Injection/test_return_values.py`, `Return_Value_and_Dependency_Injection/test_user_service.py`

- **`payment.py`**: Defines `PaymentGateway` and `OrderProcessor`. The processor receives a gateway through its constructor and uses it to process payments. It raises a `ValueError` if the payment amount is not positive.
- **`test_payment.py`**: Uses a mock payment gateway and configures its `charge()` method to return `"SUCCESS-12345"`. It verifies the order-processing result.
- **`return_value.py`**: Defines `UserService`, which receives a database dependency through its constructor and uses it to find a username.
- **`test_user_service.py`**: Uses a mock database to return `"Alice"` when `find_user()` is called.
- **`test_return_values.py`**: Uses a list assigned to `side_effect` to return different IDs (`1`, `2`, and `3`) on consecutive calls.

This section demonstrates dependency injection: instead of creating a dependency directly inside a class, the dependency is provided through its constructor. This makes it easier to replace real dependencies with mocks during testing.

### 7. Verifying Mock Calls

**File:** `Verifying_Calls/test_verify_calls.py`

This exercise demonstrates how to check whether mock methods were called and how they were called.

Topics covered:

- `assert_called()` checks whether a mock was called.
- `assert_called_once()` checks whether a mock was called exactly once.
- `assert_called_with()` verifies the arguments used in a call.
- `call_count` checks the total number of calls.

Example:

```python
from unittest.mock import Mock

def test_called_with_arguments():
    mock = Mock()
    mock.charge(100, currency="USD")

    mock.charge.assert_called_with(100, currency="USD")
```

These assertions help verify that application code interacts with its dependencies correctly.

### 8. Mocking Non-Deterministic Weather Data

**Files:** `weather/weather.py`, `weather/test_problems.py`, `weather/test_solutions.py`

- **`weather.py`**: Defines `get_temperature()`, which generates a random temperature between -10 and 40, and `describe_weather()`, which returns a weather description based on the temperature.
- **`test_problems.py`**: Tests whether the returned weather description belongs to the expected list of possible descriptions.
- **`test_solutions.py`**: Uses `unittest.mock.patch` to replace `get_temperature()` with fixed values.
- Tests freezing, cold, pleasant, and hot weather conditions.

The temperature ranges are:

| Temperature | Expected description |
| :--- | :--- |
| Below 0 | Freezing |
| 0–14 | Cold |
| 15–24 | Pleasant |
| 25 or above | Hot |

Mocking the random temperature makes it possible to test each weather condition predictably.

### 9. Patching with Decorators

**File:** `Weather_Decorator/test_weather_decorator.py`

This exercise demonstrates another way to use `unittest.mock.patch`.

- Uses `@patch("weather.get_temperature")` as a decorator above the test function.
- Receives the mock object as an argument to the test function.
- Configures the mock's `return_value` to control the temperature.
- Tests pleasant and cold weather descriptions.

This demonstrates how patching can be performed using either a context manager (`with patch(...)`) or a decorator (`@patch(...)`).

## How to Run the Tests

Run the commands from the `Lab_06_Data_Driven_and_Mocking` directory.

**Run the complete test suite:**

```bash
pytest -v
```

**Run individual test files:**

```bash
pytest test_param_fixture.py -v -s
pytest test_browsers.py -v -s
pytest test_data_driven.py -v
pytest Exercise/ -v
pytest load_data/test_csv_driven.py -v
pytest Patching_Dependencies/test_date_utils.py -v
pytest Patching_Dependencies/test_notifications.py -v
pytest Return_Value_and_Dependency_Injection/test_payment.py -v
pytest Return_Value_and_Dependency_Injection/test_return_values.py -v
pytest Return_Value_and_Dependency_Injection/test_user_service.py -v
pytest Verifying_Calls/test_verify_calls.py -v
pytest weather/test_problems.py -v
pytest weather/test_solutions.py -v
pytest Weather_Decorator/test_weather_decorator.py -v
```

**Options:**

- `-v`: Displays detailed test results.
- `-s`: Allows printed output from test functions and fixtures to appear in the terminal.

Some folders may require their own working directory or Python import-path adjustments depending on how the files are organized. If an import error occurs, check the module path and run the affected tests from the appropriate directory.

## Verified Test Summary

The final test results should be recorded after running the tests.

| Test group | Test files | Result |
| :--- | :--- | :--- |
| Parameterized fixtures | `test_param_fixture.py`, `test_browsers.py` | To verify |
| JSON-driven testing | `test_data_driven.py` | To verify |
| CSV-driven testing | `test_csv_driven.py` | To verify |
| Mock objects and side effects | `Exercise/` | To verify |
| Patching dependencies | `test_date_utils.py`, `test_notifications.py` | To verify |
| Dependency injection | `test_payment.py`, `test_user_service.py`, `test_return_values.py` | To verify |
| Verifying mock calls | `test_verify_calls.py` | To verify |
| Weather mocking | `test_problems.py`, `test_solutions.py` | To verify |
| Patching decorators | `test_weather_decorator.py` | To verify |
| **Total** | **Complete Lab 06 suite** | **Pending verification** |

The table should be updated with the actual number of passed, failed, and skipped tests after the complete test suite has been executed.

## Key Learning Outcomes

After completing this lab, I learned how to:

- Use parameterized fixtures to run tests with different configurations.
- Use `request.param` to access fixture parameters.
- Load test cases from external JSON and CSV files.
- Separate test data from test logic using data-driven testing.
- Create and configure mock objects with `unittest.mock.Mock`.
- Use `return_value` to provide fixed responses from mock methods.
- Use `side_effect` to simulate exceptions, sequential values, and custom function behavior.
- Patch dependencies using `unittest.mock.patch` and the `@patch` decorator.
- Apply dependency injection to replace real dependencies with mock objects.
- Verify mock calls using `assert_called()`, `assert_called_once()`, `assert_called_with()`, and `call_count`.
- Mock random temperature values to test different conditions predictably.
- Run individual test files and interpret Pytest results.

## Conclusion

This lab helped me understand how data-driven testing and mocking can make automated tests more flexible, predictable, and maintainable. I learned how to use external JSON and CSV files to provide test data, parameterized fixtures to test multiple configurations, and mock objects to control dependency behavior.

I also practiced patching dependencies, using dependency injection, verifying mock calls, and testing non-deterministic behavior such as random temperature values. These techniques help me test application logic independently without relying on real external services or unpredictable data.