# Automated Software Testing (192-211)

This repository contains my coursework and learning progress for the Automated Software Testing (192-211) course. It includes weekly labs, quizzes, test design exercises, and automated tests developed using Python and pytest.

## Student Information

| Item | Information |
| :--- | :--- |
| **Student** | Thida Khaing |
| **Student ID** | 6705140024 |
| **Course** | Automated Software Testing (192-211) |

## Quizzes & Labs

| Lab / Quiz | Topic | Status |
| :--- | :--- | :--- |
| [Lab 01 — Why Do We Test Software?](./Lab_01_motivation/) | Testing motivation, subtle branch defects, edge cases, and regression testing with pytest. | Completed |
| [RomanNumeral — Roman Numeral Converter](./RomanNumeral/) | Roman numeral conversion and validation using equivalence partitioning, edge cases, and exception testing. | Completed |
| [Lab 02 — Writing Effective Test Cases](./Lab_02_effective_test_cases/) | Effective test design focusing on the AAA pattern, test independence vs. shared mutable state, and boundary value analysis. | Completed |
| [Lab 03 — Descriptive Testing (Week 4)](./Lab_03_descriptive_test_Week4/) | Descriptive test organization using test classes, data-type assertion strategies, and positive/negative validation testing. | Completed |
| [Lab 04 — Fixtures and Test Setup](https://github.com/Thida-Khaing-may/st211-quizzes-6705140024/tree/main/Lab_04_Fixtures_and_Set_Up) | Reusable test setup using `@pytest.fixture`, fixture parameters, and a `BankAccount` example to reduce repeated setup code. | Completed |
| [Lab 05 — Parameterized Testing](https://github.com/Thida-Khaing-may/st211-quizzes-6705140024/tree/main/Lab_05_parameterized_testing) | Data-driven testing with `@pytest.mark.parametrize`, multiple parameter combinations, exception testing, custom test IDs, and expected failures (`xfail`). | Completed |
| [Lab 06 — Data-Driven Testing and Mocking](./Lab_06_Data_Driven_and_Mocking/) | Parameterized fixtures, JSON- and CSV-driven testing, login validation using external test data, and mocking with `unittest.mock.patch` to test predictable weather conditions. | In Progress |
| [Lab 07 — Mock Objects and Dependency Injection](./Lab_07_Mock_Objects_and_Dependency_Injection/) | Creating mock objects, using `return_value`, and testing exceptions, iterable sequences, and callable functions with `side_effect`. | Completed — 14 tests passed |


---

## Testing Topics Practiced

- **Unit Testing with pytest** — Automated test discovery, test execution, and verbose reporting (`pytest -v`).
- **AAA Pattern (Arrange, Act, Assert)** — Structuring test functions into explicit setup, execution, and verification phases.
- **Test Independence** — Ensuring test cases run in isolation without depending on shared mutable state.
- **Edge-Case & Regression Testing** — Designing targeted tests to catch subtle logic errors and prevent reintroducing defects.
- **Boundary Value Analysis (BVA)** — Evaluating system behavior at, above, and below critical input limits and grade boundaries.
- **Equivalence Partitioning** — Dividing input domains into valid and invalid representative partitions.
- **Positive and Negative Testing** — Verifying expected outcomes for valid inputs and defensive error rejection for invalid inputs.
- **Exception Assertions (`pytest.raises`)** — Asserting that invalid inputs raise specific exceptions (`ValueError`, `TypeError`).
- **Data-Type-Specific Assertions** — Utilizing floating-point tolerances (`pytest.approx`) and assertions on collections (lists, dictionaries, sets).
- **Test Organization with Test Classes** — Structuring related tests into logical test classes (`Test*`) for clean failure isolation.
- **Descriptive Test Naming** — Writing self-documenting test names that clearly convey the behavior being verified.
- **Pytest Fixtures (`@pytest.fixture`)** — Creating reusable test data and objects, injecting fixtures into test functions, and reducing repeated setup code.
- **Parameterized Testing (`@pytest.mark.parametrize`)** — Testing multiple input values and expected results with a single test function.
- **Multiple Parameter Combinations** — Using stacked parameterization decorators to generate combinations of test inputs.
- **Custom Test IDs** — Using `ids` and `pytest.param()` to make individual test cases easier to identify in test reports.
- **Expected Failure Markers (`pytest.mark.xfail`)** — Marking test cases that are expected to fail so their results can be identified separately from unexpected failures.
- **Test Output and Reporting** — Using `-v` for detailed test reports and `-s` to display printed output in the terminal.
- **Parameterized Fixtures (`@pytest.fixture(params=...)`)** — Running the same tests with multiple browser or database configurations and using `yield` for setup and teardown.
- **JSON-Driven Testing** — Loading input values and expected results from JSON files to create parameterized test cases.
- **CSV-Driven Testing** — Using Python's `csv.DictReader` to load login-validation test data from CSV files.
- **Mocking (`unittest.mock.patch`)** — Replacing dependencies with controlled return values to test specific conditions without relying on random behavior.
- **Mock Objects:** Creating and configuring mock objects with Python's `unittest.mock.Mock`.
- **Static Return Values:** Using `return_value` to return consistent results across repeated calls.
- **Exception Testing with Mocks:** Using `side_effect` to raise exceptions and checking them with `pytest.raises()`.
- **Iterable Side Effects:** Returning different values across consecutive calls and testing `StopIteration` after the iterable is exhausted.
- **Callable Side Effects:** Passing mock-call arguments to a custom function to produce dynamic results.
- **Mock Behavior Comparison:** Comparing `return_value` with exception, iterable, and callable forms of `side_effect`.


---

## Repository Structure
```text
st211-quizzes-6705140024/
├── Assignment_02/
│   ├── main.py
│   ├── rental.py
│   ├── test_rental.py
│   └── README.md
├── Lab_01_testing_fundamentals/
│   ├── Calculator_Testing/
│   │   ├── src/
│   │   ├── tests/
│   │   └── README_local_backup.md
│   ├── num_finder/
│   │   ├── num_finder.py
│   │   ├── test_num_finder.py
│   │   └── README.md
│   └── README.md
├── Lab_02_effective_test_cases/
│   ├── bank.py
│   ├── grades.py
│   ├── test_bank.py
│   ├── test_dependent.py
│   ├── test_grade.py
│   ├── test_independent.py
│   └── README.md
├── Lab_03_descriptive_test_Week4/
│   ├── Assertion_Testing/
│   │   ├── test_collections.py
│   │   ├── test_floats.py
│   │   └── README.md
│   ├── Configuration_Testing/
│   │   ├── pytest.ini
│   │   ├── shopping.py
│   │   ├── test_shopping.py
│   │   ├── test_strict.py
│   │   └── README.md
│   ├── Markers/
│   │   ├── pytest.ini
│   │   ├── test_markers.py
│   │   └── README.md
│   ├── Positive and Negative Testing/
│   │   ├── test_negative.py
│   │   ├── test_positive.py
│   │   ├── validators.py
│   │   └── README.md
│   ├── ShoppingCart/
│   │   ├── shopping.py
│   │   ├── test_shopping.py
│   │   └── README.md
│   ├── Skipping_and_Xfail/
│   │   ├── pytest.ini
│   │   ├── test_conditional.py
│   │   ├── test_skipping.py
│   │   ├── test_skips.py
│   │   ├── test_xfail.py
│   │   └── README.md
│   └── README.md
├── Lab_04_Fixtures_and_Setup/
│   ├── Fixtures/
│   │   ├── Fixtures/
│   │   │   ├── bank.py
│   │   │   └── test_after.py
│   │   └── README.md
│   └── README.md
├── Lab_05_Parameterized_Testing/
│   ├── discount.py
│   ├── mathutils.py
│   ├── test_custom_ids.py
│   ├── test_default_ids.py
│   ├── test_discount.py
│   ├── test_discount_errors.py
│   ├── test_factorial.py
│   ├── test_multi.py
│   ├── test_param.py
│   ├── test_param_ids.py
│   ├── test_param_marks.py
│   └── README.md
├── Lab_06_Data_Driven_and_Mocking/
│   ├── test_param_fixture.py
│   ├── test_browsers.py
│   ├── test_cases.json
│   ├── test_data_driven.py
│   ├── load_data/
│   │   ├── logins.csv
│   │   ├── validate.py
│   │   └── test_csv_driven.py
│   ├── weather/
│   │   ├── weather.py
│   │   ├── test_problems.py
│   │   └── test_solutions.py
│   └── README.md
├── Lab_07_Mock_Objects_and_Dependency_Injection/
│   ├── payment.py
│   ├── test_mock_basics.py
│   ├── README.md
│   └── Exercise/
│       ├── test_mock_basics.py
│       ├── test_return_value.py
│       ├── test_side_effect_exception.py
│       ├── test_side_effect_list.py
│       ├── test_side_effect_function.py
│       └── test_comparison.py
├── RomanNumeral/
│   ├── source/
│   ├── tests/
│   └── README.md
├── .gitignore
└── README.md
```
---

## Progress

- **Completed Labs**: Labs 01–05 and the RomanNumeral exercise are documented in the repository.
Lab 06 documentation has been added, and its complete test suite still needs final verification.
- **Test Suites**: The labs include dedicated pytest tests for functional behavior, edge cases, invalid inputs, exceptions, reusable fixtures, and parameterized test cases,external test data, and mocked dependencies.
- **Documentation**: Individual lab README files describe the objectives, project structure, test execution commands, results, and learning outcomes.
- **Testing Practice**: I have practiced organizing tests, reducing duplicated setup, testing multiple inputs efficiently, loading test data from JSON and CSV files, controlling dependencies with mocking, and interpreting pytest results, including expected failures.
- Practiced creating and configuring Python mock objects.
- Tested fixed responses using `return_value`.
- Simulated exceptions using `side_effect`.
- Tested sequential return values and iterable exhaustion.
- Used callable side effects to perform calculations with input arguments.
- Compared different mock configurations using pytest.



---

## Learning Outcome

Through these labs, I am developing a stronger understanding of software testing principles and automated testing with Python and pytest. I have practiced designing meaningful test cases, organizing reusable test setup, checking valid and invalid inputs, and using parameterization to improve test coverage while reducing repetitive test code.I have also learned to load test cases from JSON and CSV files, use parameterized fixtures for multiple configurations, and apply mocking to test specific conditions in a predictable way.In Lab 07, I practiced creating and configuring mock objects using Python's unittest.mock.Mock, using return_value to provide consistent results, and using side_effect to simulate exceptions, return sequential values, and execute custom functions based on input arguments.

These exercises have helped me understand how to test different behaviors in a controlled and predictable way without relying on real external dependencies. I am also improving my ability to organize test files, interpret pytest results, test edge cases and exceptions, and document testing procedures and outcomes clearly.