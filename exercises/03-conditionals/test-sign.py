import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize('value, expected', [
    *(
        (x * s, s)
        for x in range(1, 100)
        for s in [1, -1]
    ),
    (0, 0)
])
def test_sign(value, expected):
    actual = student.sign(value)

    assert expected == actual, f"sign({x}) should return {expected} but got {actual} instead"
