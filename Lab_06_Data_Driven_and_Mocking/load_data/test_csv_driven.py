import csv
from pathlib import Path
import pytest


def is_valid_login(username, password):
    # Valid if both fields are non-empty and not just spaces
    return bool(username and username.strip() and password and password.strip())

CSV_FILE = Path(__file__).parent / "logins.csv"

def load_login_cases():
    cases = []
    with open(CSV_FILE, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader, None)  # Skip header row
        for row in reader:
            if len(row) >= 3:
                
                expected_bool = row[2].strip().lower() == "true"
                cases.append((row[0].strip(), row[1].strip(), expected_bool))
    return cases


@pytest.mark.parametrize("username,password,expected", load_login_cases())
def test_login(username, password, expected):
    assert is_valid_login(username, password) == expected