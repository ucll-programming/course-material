import pytest
import student


ROCK = 0
PAPER = 1
SCISSORS = 2


@pytest.mark.timeout(1)
@pytest.mark.parametrize("player1_choice, player2_choice, expected", [
    (PAPER, PAPER, 0),
    (ROCK, ROCK, 0),
    (SCISSORS, SCISSORS, 0),
    (PAPER, ROCK, 1),
    (PAPER, SCISSORS, 2),
    (ROCK, PAPER, 2),
    (ROCK, SCISSORS, 1),
    (SCISSORS, PAPER, 1),
    (SCISSORS, ROCK, 2)
])
def test_rock_paper_scissors(player1_choice, player2_choice, expected):
    actual = student.rock_paper_scissors(player1_choice, player2_choice)
    assert expected == actual
