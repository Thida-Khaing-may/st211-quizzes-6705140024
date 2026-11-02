# from unittest.mock import Mock
# import pytest


# def test_side_effect_exception():
#     mock = Mock()
#     mock.login.side_effect = RuntimeError("Invalid credentials")
#     with pytest.raises(ValueError):
#         mock.login()
# from unittest.mock import Mock
# import pytest


# def test_side_effect_exception():
#   mock = Mock()
#   mock.login.side_effect = RuntimeError("Invalid credentials")
#   with pytest.raises(RuntimeError):
#     mock.login()

# from unittest.mock import Mock


# def test_side_effect_exception():
#     mock = Mock()
#     mock.login.side_effect = RuntimeError("Invalid credentials")
#     mock.login()

import pytest
from unittest.mock import Mock


def test_side_effect_exception_value_error():
  mock = Mock()
  mock.login.side_effect = ValueError("Invalid credentials")
  with pytest.raises(ValueError):
    mock.login()


def test_side_effect_exception_runtime_error():
  mock = Mock()
  mock.login.side_effect = RuntimeError("Invalid credentials")
  with pytest.raises(RuntimeError):
    mock.login()