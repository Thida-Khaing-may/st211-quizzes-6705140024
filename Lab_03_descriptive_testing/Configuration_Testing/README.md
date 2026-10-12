# Lab_03: Configuration Testing

- **Course:** 192-211 Automated Software Testing
- **Student:** Thida Khaing 6705140024
- **Student ID** 6705140024
- **Lab:** 03 — Configuration and Custom Markers

Overview

This folder demonstrates how to configure pytest using a pytest.ini file and how custom markers are registered and checked.

It also includes a simple ShoppingCart example to practice writing tests in a test class.

The main focus is:

pytest.ini configuration
Custom pytest markers
Strict marker validation
Basic class-based tests
Running tests with pytest
Files
File	Description
pytest.ini	Registers custom pytest markers such as smoke, slow, and regression.
shopping.py	Contains the ShoppingCart class with methods for adding items, counting items, and calculating the total price.
test_shopping.py	Contains tests for the ShoppingCart class.
test_strict.py	Demonstrates what happens when an unregistered pytest marker is used.
1. Pytest Configuration

The pytest.ini file registers the custom markers used in the project:

[pytest]

markers =
    smoke: critical path tests
    slow: tests that take a long time
    regression: tests for previously fixed bugs

Registering markers makes their purpose clear and allows pytest to check whether a marker has been defined.

2. ShoppingCart Tests

The ShoppingCart class stores items and provides two basic operations:

count() returns the number of items.
total() calculates the total price of all items.

The tests in test_shopping.py check:

A new cart starts empty.
A new cart has a total of 0.
Adding an item increases the item count.
The total price is calculated correctly.

Example:

def test_total_sum_prices(self):
    cart = ShoppingCart()
    cart.add("Book", 20)
    cart.add("Pen", 5)
    assert cart.total() == 25
3. Strict Marker Validation

The file test_strict.py uses a marker that is not registered in pytest.ini:

@pytest.mark.nonexistent_marker
def test_bad_marker():
    assert True

This is included to demonstrate the difference between normal pytest execution and strict marker validation.

Normal pytest

Running:

python -m pytest test_strict.py -v

allows the test to run, but pytest reports an UnknownMarkWarning because nonexistent_marker has not been registered.

Strict marker mode

Running:

python -m pytest test_strict.py --strict-markers

causes pytest to stop during test collection because nonexistent_marker is not registered in pytest.ini.

This helps detect misspelled or incorrectly registered markers.

How to Run

Open the terminal in this folder and run:

Run the ShoppingCart tests
python -m pytest test_shopping.py -v
Run the marker example normally
python -m pytest test_strict.py -v

This demonstrates the unknown-marker warning.

Run with strict marker validation
python -m pytest test_strict.py --strict-markers

This is expected to produce a collection error because nonexistent_marker is intentionally not registered.

Run all tests in the folder
python -m pytest -v
Expected Result

The ShoppingCart tests should pass.

The test_strict.py test is intentionally used to demonstrate pytest marker validation. Therefore, when strict marker checking is enabled, a collection error is expected.

What I Practiced

In this exercise, I practiced:

Creating a pytest.ini configuration file.
Registering custom pytest markers.
Writing class-based tests.
Running specific test files with pytest.
Understanding unknown marker warnings.
Using --strict-markers to detect unregistered markers.