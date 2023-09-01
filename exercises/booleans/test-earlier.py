import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("h1, m1, h2, m2, expected", [
    (k1 // 60, k1 % 60, k2 // 60, k2 % 60, k1 < k2)
    for k1 in range(0, 12 * 60, 25)
    for k2 in range(0, 12 * 60, 25)
])
def test_earlier(h1, m1, h2, m2, expected):
    actual = student.earlier(h1, m1, h2, m2)
    assert expected == actual, f'{h1:02}:{m1:02} should be earlier than {h2:02}:{m2:02}'
