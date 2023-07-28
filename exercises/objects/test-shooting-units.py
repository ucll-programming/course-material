import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("health", [0, 5, 10, 100])
@pytest.mark.parametrize("firepower", [0, 1, 2, 10])
@pytest.mark.parametrize("armor", [0, 2, 5])
def test_valid_initialization(health, firepower, armor):
    unit = student.Unit(health=health, firepower=firepower, armor=armor)
    assert unit.health == health
    assert unit.firepower == firepower
    assert unit.armor == armor


@pytest.mark.timeout(1)
@pytest.mark.parametrize("health, firepower, armor", [
    (-1, 50, 2),
    (5, -5, 2),
    (5, 5, -1),
])
def test_invalid_initialization(health, firepower, armor):
    with pytest.raises(ValueError):
        student.Unit(health=health, firepower=firepower, armor=armor)


@pytest.mark.timeout(1)
@pytest.mark.parametrize("b_health, b_armor, a_firepower, expected_b_health", [
    (100, 0, 1, 99),
    (100, 0, 2, 98),
    (100, 0, 10, 90),
    (100, 5, 10, 95),
    (50, 5, 10, 45),
    (50, 6, 10, 46),
    (50, 15, 10, 50),
    (5, 0, 10, 0),
])
@pytest.mark.parametrize("a_health", [5, 10])
@pytest.mark.parametrize("a_armor", [0, 2])
@pytest.mark.parametrize("b_firepower", [0, 2])
def test_shot_by(a_health, a_firepower, a_armor, b_health, b_armor, b_firepower, expected_b_health):
    # Arrange
    unit_a = student.Unit(health=a_health, firepower=a_firepower, armor=a_armor)
    unit_b = student.Unit(health=b_health, firepower=b_firepower, armor=b_armor)

    # Act
    unit_b.shot_by(unit_a)

    # Assert
    assert expected_b_health == unit_b.health
    assert a_health == unit_a.health
    assert a_firepower == unit_a.firepower
    assert a_armor == unit_a.armor
    assert b_firepower == unit_b.firepower
    assert b_armor == unit_b.armor
