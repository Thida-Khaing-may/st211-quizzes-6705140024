# from unittest.mock import Mock
# def test_side_effect_list():
#     mock = Mock()
#     # mock.get_data.side_effect = [
#     #     "A",
#     #     "B",
#     #     "C"
#     # ]
#     mock.get_data.return_value = [
#         "A",
#         "B",
#         "C"
#     ]
#     #mock.get_data.side_effect = [1, 2]
    
#     assert mock.get_data() == "A"
#     assert mock.get_data() == "B"
#     assert mock.get_data() == "C"
    
#     print(mock.get_data())
import pytest
from unittest.mock import Mock


def test_side_effect_list_sequence():
  mock = Mock()
  mock.get_data.side_effect = ["A", "B", "C"]
  assert mock.get_data() == "A"
  assert mock.get_data() == "B"
  assert mock.get_data() == "C"


def test_side_effect_list_stop_iteration():
  mock = Mock()
  mock.get_data.side_effect = [1, 2]
  assert mock.get_data() == 1
  assert mock.get_data() == 2
  with pytest.raises(StopIteration):
    mock.get_data()