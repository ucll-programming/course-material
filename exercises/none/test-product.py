import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("a, b, c, expected", [
    *(
        (a, b, c, a * b * c)
        for a in [0, 1, 4, 10]
        for b in [0, 1, 2, 15]
        for c in [0, 1, 5, 19]
    ),
    *(
        (a, b, None, a * b)
        for a in [0, 1, 4, 10]
        for b in [0, 1, 2, 15]
    ),
    *(
        (a, None, b, a * b)
        for a in [0, 1, 4, 10]
        for b in [0, 1, 2, 15]
    ),
    *(
        (None, a, b, a * b)
        for a in [0, 1, 4, 10]
        for b in [0, 1, 2, 15]
    ),
    *(
        (None, None, a, a)
        for a in [0, 1, 9]
    ),
    *(
        (None, a, None, a)
        for a in [0, 1, 9]
    ),
    *(
        (a, None, None, a)
        for a in [0, 1, 9]
    ),
    (
        (None, None, None, 1)
    )
])
def test_product(a, b, c, expected):
    actual = student.product(a, b, c)
    assert expected == actual, f'product({a}, {b}, {c}) should return {expected} but got {actual}'
