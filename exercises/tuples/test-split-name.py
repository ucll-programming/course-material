import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("full_name, expected", [
    (f'{first_name} {last_name}', (first_name, last_name))
    for first_name, last_name in [
        ('Jon', 'Snow'),
        ('Tyrion', 'Lannister'),
        ('Daenerys', 'Targaryen'),
        ('Ned', 'Stark'),
    ]
])
def test_split_name(full_name, expected):
    actual = student.split_name(full_name)
    assert expected == actual
