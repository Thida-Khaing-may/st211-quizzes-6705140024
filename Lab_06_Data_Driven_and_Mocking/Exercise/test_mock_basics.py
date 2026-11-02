from unittest.mock import Mock

def test_mock_basics():
  mock = Mock()
  result = mock.anything()
  assert isinstance(result, Mock)


def test_mock_accepts_arguments():
  mock = Mock()
  result = mock.whatever(1, 2, 3)
  assert isinstance(result, Mock)