import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("x, y, expected", [
    (1, 1, 1),
    *(
        triple
        for x, y, r in [
            (12, 16, 4),
            (40, 20, 20),
            (20, 25, 5),
            (100, 100, 100),
            (17, 31, 1),
            (17 * 31 * 97, 17 * 37 * 97, 17 * 97),
            (10**100, 10**200, 10**100),
        ]
        for sx in [-1, 1]
        for sy in [-1, 1]
        for triple in [
            (x * sx, y * sy, r),
            (y * sy, x * sx, r),
        ]
    )
])
def test_gcd(x, y, expected):
    actual = student.gcd(x, y)

    assert expected == actual, f"gcd({x}, {y}) should be {expected} but was {actual}"
