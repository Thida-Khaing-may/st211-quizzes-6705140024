import pytest
from source.roman import convert


# Category 1 - Single symbol
def test_single_symbol():
    assert convert("I") == 1
    assert convert("V") == 5


# Category 2 - Repeated symbols
def test_repeated_symbols():
    assert convert("II") == 2
    assert convert("III") == 3


# Category 3 - Different symbols
def test_different_symbols():
    assert convert("VI") == 6
    assert convert("XVI") == 16


# Category 4 - Subtractive notation
def test_subtractive_notation():
    assert convert("IV") == 4
    assert convert("IX") == 9


# Category 5 - Digit + subtractive notation
def test_digit_plus_subtractive():
    assert convert("XIX") == 19


# Category 6 - Invalid input
def test_invalid_input():

    with pytest.raises(ValueError):
        convert("VX")

    with pytest.raises(ValueError):
        convert("XXC")

    with pytest.raises(ValueError):
        convert("IIII")

    with pytest.raises(ValueError):
        convert("VV")

    with pytest.raises(ValueError):
        convert("ABC")

    with pytest.raises(ValueError):
        convert("")

    with pytest.raises(TypeError):
        convert(123)
        