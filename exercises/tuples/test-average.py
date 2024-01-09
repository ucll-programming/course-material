import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("ns", [
    (0,),
    (1,),
    (1, 3),
    (1, 2, 3),
    (1, 2),
    (9, 4, 1, 2, 8, 6),
    (48, 132, 78, 46, 13, 16, 85),
    (1000, 5000),
])
def test_average(ns):
    actual = student.average(ns)
    assert actual * len(ns) == pytest.approx(sum(ns))
