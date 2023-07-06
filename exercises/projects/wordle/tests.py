import pytest
import student


@pytest.mark.parametrize("actual, guess, expected_judgement_string", [
    ("A", "A", "C"),
    ("A", "B", "X"),
    ("AA", "AA", "CC"),
    ("AB", "AB", "CC"),
    ("AB", "BA", "MM"),
    ("AB", "BX", "MX"),
    ("ABCDE", "ABCDE", "CCCCC"),
    ("ABCDE", "BCDEA", "MMMMM"),
    ("ABCDE", "BXDEA", "MXMMM"),
    ("AABCD", "ABCAA", "CMMMX"),
    ("AABCD", "BCDAA", "MMMMM"),
    ("ABABA", "BABAB", "MMMMX"),
])
def test_judge(actual, guess, expected_judgement_string):
    def parse_judgement(char: str) -> student.Judgement:
        match char:
            case "C":
                return student.Judgement.CORRECT
            case "M":
                return student.Judgement.MISPLACED
            case "X":
                return student.Judgement.WRONG

    actual_judgement = student.judge(actual, guess)
    expected_judgement = [parse_judgement(judgement) for judgement in expected_judgement_string]
    assert expected_judgement == actual_judgement
