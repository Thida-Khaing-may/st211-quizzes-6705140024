# from unittest.mock import Mock


# def test_mock_basics():
#   mock = Mock()
#   result = mock.anything()
#   print(result)
#   assert isinstance(result, Mock)


# from unittest.mock import Mock


# def test_return_value():
#   mock = Mock()
#   mock.get_status.return_value = "FAILED"
#   assert mock.get_status() == "OK"  # Fails!

from unittest.mock import Mock


def test_return_value_string():
  mock = Mock()
  mock.get_status.return_value = "OK"
  assert mock.get_status() == "OK"


def test_return_value_integer():
  mock = Mock()
  mock.get_status.return_value = 123
  assert mock.get_status() == 123

  