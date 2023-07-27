import pytest
import student


def test_private_field():
    password = student.Password('abc')
    assert not hasattr(password, 'password'), 'Password should not have public field password'
    assert hasattr(password, '_Password__password'), 'Password should have private field password'


@pytest.mark.timeout(1)
def test_verify():
    password = student.Password('xyz')
    assert password.verify('xyz')
    assert not password.verify('abc')
