import pytest
from unittest.mock import Mock


def test_comparison_return_value():
  mock = Mock()
  mock.fetch.return_value = "STATIC"
  assert mock.fetch() == "STATIC"
  assert mock.fetch() == "STATIC"


def test_comparison_side_effect_list():
  mock = Mock()
  mock.fetch.side_effect = ["A", "B", "C"]
  assert mock.fetch() == "A"
  assert mock.fetch() == "B"
  assert mock.fetch() == "C"


def test_comparison_side_effect_exception():
  mock = Mock()
  mock.fetch.side_effect = RuntimeError("Boom")
  with pytest.raises(RuntimeError):
    mock.fetch()


def test_comparison_side_effect_function():
  mock = Mock()

  def fetch(value):
    return value.upper()

  mock.fetch.side_effect = fetch
  assert mock.fetch("hello") == "HELLO"

