# Automated Software Testing (192-211)

This repository contains my coursework and learning progress for the Automated Software Testing (192-211) course. It includes weekly labs, quizzes, test design exercises, and automated tests developed using Python and `pytest`.

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

## Repository Structure

```text
.
├── Lab_01_motivation/
├── Lab_02_effective_test_cases/
├── Lab_03_descriptive_test_Week4/
├── RomanNumeral/
└── README.md
```

## Progress

- **Completed Labs**: 4 laboratory modules (Weeks 1 through 4) are implemented and documented in the repository.
- **Test Suites**: Each lab includes dedicated `pytest` test suites verifying functional requirements, edge cases, and exception handling.
- **Documentation**: Each lab directory contains an individual `README.md` detailing core concepts, test matrices, execution instructions, and learning outcomes.

