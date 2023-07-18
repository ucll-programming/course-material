import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("grade1, grade2, grade3, grade4, grade5, expected", [
    (12, 12, 12, 12, 12, True),
    (10, 10, 10, 10, 10, False),
    (11, 12, 12, 12, 12, False),
    (None, 12, 12, 12, 12, True),
    (15, 17, 18, 13, 15, True),
    (15, None, 18, 13, 15, True),
    (15, 17, None, 13, 15, True),
    (15, 17, 18, None, 15, True),
    (15, 17, 18, 13, None, True),
    (20, 20, 20, None, None, False),
    (20, None, 20, None, 20, False),
    (None, None, None, None, None, False),
])
def test_entrance_exam(grade1, grade2, grade3, grade4, grade5, expected):
    actual = student.entrance_exam(grade1, grade2, grade3, grade4, grade5)
    assert expected == actual, f'entrance_exam({grade1}, {grade2}, {grade3}, {grade4}, {grade5}) should return {expected}'
