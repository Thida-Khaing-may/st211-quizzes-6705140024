from unittest.mock import Mock


def test_was_called():
    mock = Mock()
    mock.save()
    mock.save.assert_called()


def test_was_called_once():
    mock = Mock()
    mock.save()
    mock.save.assert_called_once()# exactly one

# def test_was_called_once_fails_on_two_calls():
#     mock = Mock()
#     mock.save()
#     mock.save()  # Second call causes the failure
#     mock.save.assert_called_once()

def test_called_with_arguments():
    mock = Mock()
    mock.charge(100, currency="USD")
    mock.charge.assert_called_with(100, currency="USD")
def test_call_count():
    mock = Mock()
    mock.log()
    mock.log()
    assert mock.log.call_count == 2