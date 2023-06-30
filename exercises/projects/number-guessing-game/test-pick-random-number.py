import pytest
from testlib import *
import student


@pytest.mark.parametrize('expected', range(1, 101))
def test_pick_random_number(fake_random, expected):
    fake_random([expected])
    actual = student.pick_random_number()

    assert expected == actual
