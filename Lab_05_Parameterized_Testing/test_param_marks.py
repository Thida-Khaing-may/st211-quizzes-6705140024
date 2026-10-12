import pytest


@pytest.mark.parametrize("value,expected",[
    pytest.param(2, 4, id="two_squared"),
    pytest.param(3, 9, id="three_squared"),
    pytest.param(5, 20, id="known_bug",
                marks=pytest.mark.xfail),
    

])
def test_square(value,expected):
    assert value ** 2 == expected
    