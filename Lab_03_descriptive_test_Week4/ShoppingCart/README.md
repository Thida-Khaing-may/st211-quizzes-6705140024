# ShoppingCart — Organizing Tests with Test Classes

- **Course:** 192-211 Automated Software Testing
- **Student:** Thida Khaing 6705140024
- **Lab:** Week 4 — Descriptive Testing
- **Exercise:** ShoppingCart — Organized Tests


---

## 1. Purpose

The purpose of this exercise is to demonstrate how to organize related unit tests inside a `pytest` test class (`TestShoppingCart`) and verify the behavior of the `ShoppingCart` class. 


---

## 2. Project Files

This exercise consists of two Python files located in the `ShoppingCart` folder:

- **`shopping.py`**: The implementation file containing the `ShoppingCart` class. It manages cart items, calculates totals, and tracks item counts.
- **`test_shopping.py`**: The test suite containing automated unit tests structured within the `TestShoppingCart` class using `pytest`.

---

## 3. ShoppingCart Class

The `ShoppingCart` class provides a simple model of an e-commerce shopping cart. Its purpose is to store items added by a user, provide the total price of all items, and report the current number of items.

### Method Breakdown

| Method | Purpose |
| :--- | :--- |
| `__init__()` | Initializes a new shopping cart with an empty items list (`self.items = []`). |
| `add(name, price)` | Adds a single item represented as a dictionary `{"name": name, "price": price}` to the cart. |
| `total()` | Computes and returns the sum of the prices of all items in the cart. Returns `0` if empty. |
| `count()` | Returns the total number of items currently in the cart. |

---

## 4. How ShoppingCart Works

The `ShoppingCart` class relies on a simple list of dictionaries to manage state:

### 1. Initialization
When a new `ShoppingCart` object is instantiated, `__init__()` sets `self.items` as an empty Python list:
```python
def __init__(self):
    self.items = []
```

### 2. Adding Items
The `add(name, price)` method creates a dictionary containing the item's name and price, then appends it to `self.items`:
```python
def add(self, name, price):
    self.items.append({"name": name, "price": price})
```

### 3. Calculating the Total
The `total()` method uses a generator expression inside Python's built-in `sum()` function to iterate over each item in `self.items` and aggregate their prices:
```python
def total(self):
    return sum(item["price"] for item in self.items)
```
If `self.items` is empty, `sum()` defaults to `0`.

### 4. Counting Items
The `count()` method calls Python's `len()` function on the internal `self.items` list:
```python
def count(self):
    return len(self.items)
```

---

## 5. Test Class

In `test_shopping.py`, all unit tests are grouped inside a single class:

```python
class TestShoppingCart:
    ...
```

### Why Group Tests Inside `TestShoppingCart`?

1. **Logical Cohesion**: All tests directly related to testing the `ShoppingCart` class are contained in one place, separating them from other features or classes.
2. **Clear Test Output**: In pytest's test output (especially with `-v`), pytest outputs the class hierarchy (e.g., `test_shopping.py::TestShoppingCart::test_new_cart_is_empty`), making it clear which component is under test.
3. **Scoping and Extensibility**: Grouping tests in a class allows easy application of class-level fixtures, configuration, or setup/teardown methods (`setup_method`) if the test suite expands.
4. **Namespace Management**: Test methods and any helper methods are cleanly contained inside the class rather than polluting the global module namespace.

---

## 6. Pytest Test Naming Rules

Pytest uses automated test discovery based on specific naming conventions. The files in this exercise follow these exact rules:

- **Test file starts with `test_`**: The file is named `test_shopping.py`. Pytest scans directories for files matching `test_*.py` or `*_test.py`.
- **Test class starts with `Test`**: The class is named `TestShoppingCart`. Pytest discovers test classes whose names begin with `Test` (capital `T`, PascalCase).
- **Test methods start with `test_`**: Each test method starts with `test_` (e.g., `test_new_cart_is_empty`, `test_total_sums_prices`). Methods without this prefix are ignored during test collection.
- **Test methods use `self`**: Because the tests are methods inside a class, each method accepts `self` as its first parameter in accordance with Python's instance method rules.
- **There is no `__init__()` in the test class**: Pytest instantiates test classes dynamically. If an `__init__()` constructor is defined in a test class, pytest will skip the class and display a warning.

---

## 7. Test Cases

There are four specific test methods implemented inside `TestShoppingCart`:

### 1. `test_new_cart_is_empty`
- **What it tests**: Verifies that a newly created shopping cart contains zero items.
- **Action performed**: A new `ShoppingCart()` instance is created, and `cart.count()` is called.
- **Assertion checked**: `assert cart.count() == 0`
- **Why it is important**: It ensures the constructor initializes an empty cart and that no leftover items or default values exist.

### 2. `test_new_cart_total_is_zero`
- **What it tests**: Verifies that the monetary total of a newly created cart is zero.
- **Action performed**: A new `ShoppingCart()` instance is created, and `cart.total()` is called.
- **Assertion checked**: `assert cart.total() == 0`
- **Why it is important**: It confirms that calculating the total on an empty list safely returns `0` rather than raising an exception or returning `None`.

### 3. `test_add_item_increases_count`
- **What it tests**: Verifies that adding an item increases the cart's item count by 1.
- **Action performed**: A new `ShoppingCart()` is created, and `cart.add("Book", 20)` is executed.
- **Assertion checked**: `assert cart.count() == 1`
- **Why it is important**: It validates state mutation, confirming that `add()` successfully updates the cart contents and reflects in `count()`.

### 4. `test_total_sums_prices`
- **What it tests**: Verifies that the total calculation correctly sums the prices of multiple items.
- **Action performed**: A new `ShoppingCart()` is created, and two items are added: `"Book"` with price `20` and `"Pen"` with price `5`.
- **Assertion checked**: `assert cart.total() == 25` (since $20 + 5 = 25$).
- **Why it is important**: It ensures that `total()` correctly iterates through all added items and computes the mathematical sum of their prices without dropping or miscalculating values.

---

## 8. Arrange-Act-Assert (AAA)

The **Arrange-Act-Assert** pattern divides every test into three clear steps:

1. **Arrange**: Prepare the object, test data, and prerequisites.
2. **Act**: Execute the method or behavior being tested.
3. **Assert**: Verify that the actual outcome matches the expected outcome.

### Examples from `test_shopping.py`

#### Example A: Testing Initial State (`test_new_cart_is_empty`)
```python
def test_new_cart_is_empty(self):
    # Arrange: Create a fresh cart
    cart = ShoppingCart()
    
    # Act: Retrieve the count
    result = cart.count()
    
    # Assert: Check that the count is 0
    assert result == 0
```

#### Example B: Testing State Change and Calculation (`test_total_sums_prices`)
```python
def test_total_sums_prices(self):
    # Arrange: Create a fresh cart
    cart = ShoppingCart()
    
    # Act: Add items with known prices
    cart.add("Book", 20)
    cart.add("Pen", 5)
    
    # Assert: Check that total() equals 20 + 5 = 25
    assert cart.total() == 25
```

---

## 9. Test Independence

Each test method in `TestShoppingCart` explicitly instantiates its own cart object (`cart = ShoppingCart()`).

### Why Test Independence Matters:
- **No Shared Mutable State**: If tests shared a single cart instance (e.g., as a class attribute or global variable), the items added in `test_add_item_increases_count` or `test_total_sums_prices` would remain in the cart for subsequent tests.
- **Order Independence**: Tests must be able to run in any order, in parallel, or individually without affecting one another.
- **Deterministic Results**: If a test fails, isolation ensures that the failure is caused by a bug in the code under test, not by side effects from a previous test.

---

## 10. Assertions

In pytest, test verification is performed using standard Python `assert` statements with equality operators:

```python
assert cart.count() == 0
assert cart.total() == 0
assert cart.count() == 1
assert cart.total() == 25
```

### What Happens During an Assertion?

- **When the assertion is `True`**:
  The condition evaluates to `True`, meaning the actual output matches the expected output. Pytest continues to the next line of code or completes the test method as **PASSED**.
- **When the assertion is `False`**:
  The condition evaluates to `False`. An `AssertionError` is raised immediately, halting that test method and marking it as **FAILED**.
- **Pytest Assertion Rewriting**:
  Pytest intercepts the `assert` statement and provides a detailed error message showing the actual vs. expected values (e.g., `assert 20 == 25`), making debugging straightforward without requiring specialized helper methods like `self.assertEqual()`.

---

## 11. How to Run the Tests

To run the tests using `pytest`, open a terminal, navigate to the `ShoppingCart` folder, and execute any of the following commands:

```bash
cd "Lab_03_descriptive_test_Week4/ShoppingCart"
```

### 1. Run all tests in the current folder:
```bash
pytest
```

### 2. Run tests with verbose output:
```bash
pytest -v
```

### 3. Run tests in a specific file:
```bash
pytest test_shopping.py -v
```

### 4. Run only the `TestShoppingCart` class:
```bash
pytest test_shopping.py::TestShoppingCart -v
```

### What Does `-v` Mean?
The `-v` flag stands for **verbose**. By default, pytest outputs a simple dot (`.`) for each passed test. When `-v` is used, pytest displays the full test file name, class name, individual test method name, and status (e.g., `PASSED` or `FAILED`), providing much clearer feedback during test runs.

---

## 12. Expected Test Result

There are **exactly 4 test methods** defined in `test_shopping.py`:

1. `test_new_cart_is_empty`
2. `test_new_cart_total_is_zero`
3. `test_add_item_increases_count`
4. `test_total_sums_prices`

### Logical Evaluation of the Tests

When executed against the current implementation in `shopping.py`:

- `test_new_cart_is_empty`: calls `count()` on `self.items = []`, evaluating `0 == 0` &rarr; Condition is `True`.
- `test_new_cart_total_is_zero`: calls `total()` on `self.items = []`, evaluating `0 == 0` &rarr; Condition is `True`.
- `test_add_item_increases_count`: adds 1 item and calls `count()`, evaluating `1 == 1` &rarr; Condition is `True`.
- `test_total_sums_prices`: adds items priced `20` and `5` and calls `total()`, evaluating `25 == 25` &rarr; Condition is `True`.

When running `pytest -v` in a configured Python environment, pytest collects and executes all 4 tests under `TestShoppingCart`, with each test passing successfully.

---

## 13. Key Learning Outcomes

This exercise reinforces several essential principles of automated software testing:

- **Test Organization**: Structuring related unit tests into cohesive test classes.
- **Test Classes**: Using classes to group test cases for a specific domain model.
- **Pytest Naming Conventions**: Applying standard discovery rules (`test_*.py`, `Test*` classes, `test_*` methods).
- **Assertions**: Writing readable, direct assertions using Python's native `assert` statement.
- **Test Independence**: Creating fresh object instances per test to prevent test interference and order dependency.
- **Testing Object State**: Verifying baseline/initial attributes and default behavior of objects.
- **Testing State Changes**: Validating that method calls mutate state predictably and return correct values.

---

## 14. Conclusion

Organizing tests inside test classes provides structure and hierarchy to automated test suites. As codebases grow to include dozens or hundreds of classes and services, grouping related test cases together prevents cluttered test files, simplifies test execution, and clarifies test reports. Ensuring complete test independence and following standard naming conventions creates reliable, maintainable test suites that are easy to expand as new features are added.
