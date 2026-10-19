import csv
import pytest
from validate import is_valid_login

def load_login_cases():
    cases = []
    with open("logins.csv") as f:
        for row in csv.DictReader(f):
            expected = row["valid"] == "True"
            cases.append((row["username"], row["password"], expected))
    return cases

@pytest.mark.parametrize("username,password,expected", load_login_cases())
def test_login_validation(username, password, expected):
    assert is_valid_login(username, password) == expected