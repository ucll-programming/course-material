import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("address", [
    "abc@gmail.com",
    "test@hotmail.com",
])
def test_initialization(address):
    email_address = student.EmailAddress(address)
    assert address == str(email_address)


@pytest.mark.timeout(1)
@pytest.mark.parametrize("address", [
    "test.gmail.com",
    "test@gmail@com",
])
def test_invalid_initialization(address):
    with pytest.raises(ValueError):
        student.EmailAddress(address)


@pytest.mark.timeout(1)
@pytest.mark.parametrize("address1, address2", [
    *(
        (student.EmailAddress(address1), student.EmailAddress(address2))
        for address1, address2 in [
            ('a@gmail.com', 'a@gmail.com'),
            ('A@gmail.com', 'a@gmail.com'),
            ('a@gmail.com', 'A@gmail.com'),
            ('aBc@yAhOo.NeT', 'abC@YaHOO.nET'),
        ]
    )
])
def test_equality(address1, address2):
    assert address1 == address2


@pytest.mark.timeout(1)
@pytest.mark.parametrize("address1, address2", [
    *(
        (student.EmailAddress(address1), student.EmailAddress(address2))
        for address1, address2 in [
            ('a@gmail.com', 'b@gmail.com'),
            ('a@yahoo.com', 'b@gmail.com'),
        ]
    )
])
def test_inequality(address1, address2):
    assert address1 != address2


@pytest.mark.timeout(1)
@pytest.mark.parametrize('address', [
    'test@gmail.com',
    'foo@geocities.net',
])
def test_repr(address):
    email_address = student.EmailAddress(address)
    actual = repr(email_address)
    assert actual in [
        f"EmailAddress('{address}')",
        f'EmailAddress("{address}")'
    ]
