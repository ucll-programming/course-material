import pytest
import student


@pytest.mark.parametrize("string", [
    "",
    "()",
    "(())",
    "()()",
    "(()())",
    "((((()))))",
])
def test_valid_parentheses(string):
    actual = student.valid_parentheses(string)

    assert actual == True, f"valid_parentheses({string}) should return True"


@pytest.mark.parametrize("string", [
    ")",
    "(",
    ")(",
    "(((()))))",
    "(((()))))(",
    "((()()()())",
])
def test_not_valid_parentheses(string):
    actual = student.valid_parentheses(string)

    assert actual == False, f"valid_parentheses({string}) should return False"
