import pytest
import student


@pytest.mark.timeout(1)
def test_ingredients():
    actual = student.ingredients()

    assert isinstance(actual, dict)
    assert len(actual) == 5
    assert 'chocolate' in actual
    assert 'eggs' in actual
    assert 'sugar' in actual
    assert 'flour' in actual
    assert 'butter' in actual
    assert actual['chocolate'] == '250g'
    assert actual['eggs'] == '5'
    assert actual['sugar'] == '125g'
    assert actual['flour'] == '75g'
    assert actual['butter'] == '175g'
