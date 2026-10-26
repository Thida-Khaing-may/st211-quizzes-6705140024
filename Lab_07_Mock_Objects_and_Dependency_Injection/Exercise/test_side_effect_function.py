from unittest.mock import Mock


def double(x):
  return x * 2


def test_side_effect_function():
  mock = Mock()
  mock.calculate.side_effect = double
  assert mock.calculate(5) == 10