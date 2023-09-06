import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("my_pattern, opponent_pattern, expected", [
    ("TTH", "TTT", 50),
    ("THT", "TTT", 60),
    ("THH", "TTT", 60),
    ("HTT", "TTT", 88),
    ("HTH", "TTT", 58),
    ("HHT", "TTT", 70),
    ("HHH", "TTT", 50),
    ("TTT", "TTH", 50),
    ("THT", "TTH", 34),
    ("THH", "TTH", 34),
    ("HTT", "TTH", 75),
    ("HTH", "TTH", 38),
    ("HHT", "TTH", 50),
    ("HHH", "TTH", 30),
    ("TTT", "THT", 40),
    ("TTH", "THT", 67),
    ("THH", "THT", 50),
    ("HTT", "THT", 50),
    ("HTH", "THT", 50),
    ("HHT", "THT", 62),
    ("HHH", "THT", 42),
    ("TTT", "THH", 40),
    ("TTH", "THH", 66),
    ("THT", "THH", 50),
    ("HTT", "THH", 50),
    ("HTH", "THH", 50),
    ("HHT", "THH", 25),
    ("HHH", "THH", 13),
    ("TTT", "HTT", 12),
    ("TTH", "HTT", 25),
    ("THT", "HTT", 50),
    ("THH", "HTT", 50),
    ("HTH", "HTT", 50),
    ("HHT", "HTT", 67),
    ("HHH", "HTT", 40),
    ("TTT", "HTH", 42),
    ("TTH", "HTH", 63),
    ("THT", "HTH", 50),
    ("THH", "HTH", 50),
    ("HTT", "HTH", 50),
    ("HHT", "HTH", 67),
    ("HHH", "HTH", 40),
    ("TTT", "HHT", 30),
    ("TTH", "HHT", 50),
    ("THT", "HHT", 38),
    ("THH", "HHT", 75),
    ("HTT", "HHT", 33),
    ("HTH", "HHT", 33),
    ("HHH", "HHT", 50),
    ("TTT", "HHH", 50),
    ("TTH", "HHH", 70),
    ("THT", "HHH", 58),
    ("THH", "HHH", 88),
    ("HTT", "HHH", 60),
    ("HTH", "HHH", 60),
    ("HHT", "HHH", 50)
])
def test_winning_percentage(my_pattern, opponent_pattern, expected):
    actual = student.winning_percentage(my_pattern, opponent_pattern, 1000)
    assert pytest.approx(expected, abs=5) == actual


@pytest.mark.timeout(1)
@pytest.mark.parametrize("opponent_pattern, expected", [
    ("TTT", "HTT"),
    ("TTH", "HTT"),
    ("THT", "TTH"),
    ("THH", "TTH"),
    ("HTT", "HHT"),
    ("HTH", "HHT"),
    ("HHT", "THH"),
    ("HHH", "THH")
])
def test_best_pattern(opponent_pattern, expected):
    actual = student.find_best_pattern(opponent_pattern)
    assert expected == actual
