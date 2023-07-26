import pytest
import student


def test_initialization():
    pair = student.Pair()
    assert hasattr(pair, 'first')
    assert hasattr(pair, 'second')
    assert pair.first is None
    assert pair.second is None
