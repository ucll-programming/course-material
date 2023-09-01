import pytest
import student


@pytest.mark.timeout(1)
def test_five():
    assert student.five() == 5
