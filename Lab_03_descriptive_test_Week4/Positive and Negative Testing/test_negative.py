
import pytest
from validators import validate_email, validate_age


def test_email_without_at_rejected():
    with pytest.raises(ValueError):
        validate_email("notanemail.com")


def test_email_without_domain_rejected():
    with pytest.raises(ValueError):
        validate_email("user@")


def test_email_without_username_rejected():
    with pytest.raises(ValueError):
        validate_email("@gmail.com")


def test_email_without_dot_rejected():
    with pytest.raises(ValueError):
        validate_email("user@gmail")


def test_email_with_one_letter_extension_rejected():
    with pytest.raises(ValueError):
        validate_email("user@gmail.c")


def test_email_with_space_rejected():
    with pytest.raises(ValueError):
        validate_email("user name@gmail.com")


def test_email_without_extension_rejected():
    with pytest.raises(ValueError):
        validate_email("user@gmail.")


def test_empty_email_rejected():
    with pytest.raises(ValueError):
        validate_email("")


def test_negative_age_rejected():
    with pytest.raises(ValueError):
        validate_age(-5)


def test_age_over_150_rejected():
    with pytest.raises(ValueError):
        validate_age(151)


def test_age_as_string_rejected():
    with pytest.raises(TypeError):
        validate_age("twenty")


def test_age_as_float_rejected():
    with pytest.raises(TypeError):
        validate_age(25.5)


def test_age_as_none_rejected():
    with pytest.raises(TypeError):
        validate_age(None)


def test_age_as_list_rejected():
    with pytest.raises(TypeError):
        validate_age([25])
