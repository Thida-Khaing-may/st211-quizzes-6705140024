import json
import pytest

def load_cases():
    with open("test_cases.json") as f:
        data = json.load(f) # read the whole file
    return [(case["input"], case["expected"]) for case in data]

@pytest.mark.parametrize("text,expected", load_cases()) # loader runs at collection
def test_uppercase(text, expected):
    assert text.upper() == expected
