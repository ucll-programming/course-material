import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize('age', [
    *range(0, 6),
    *range(65, 200),
])
def test_free_ticket(age):
    assert student.free_ticket(age)


@pytest.mark.timeout(1)
@pytest.mark.parametrize('age', range(6, 65))
def test_no_free_ticket(age):
    assert not student.free_ticket(age)
