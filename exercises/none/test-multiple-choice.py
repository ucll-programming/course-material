import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("right_answer, given_answer, expected", [
    *(
        (x, x, 1)
        for x in range(1, 6)
    ),
    *(
        (x, y, -0.2)
        for x in range(1, 6)
        for y in range(1, 6)
        if x != y
    ),
    *(
        (x, None, 0)
        for x in range(1, 6)
    )
])
def test_multiple_choice(right_answer, given_answer, expected):
    actual = student.multiple_choice(right_answer=right_answer, given_answer=given_answer)
    assert expected == actual, f'multiple_choice({right_answer}, {given_answer}) should return {expected} but got {actual}'
