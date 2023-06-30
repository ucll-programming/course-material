import pytest
from testlib import *
import student


def test_player_guesses_ai_number(read_stdout, fake_random, fake_input):
    fake_random([50])
    fake_input([50])

    student.player_guesses_ai_number()

    actual_output = read_stdout()
    expected_output = ['You guessed my number!']
    assert actual_output == expected_output


def test_player_guesses_ai_number2(read_stdout, fake_random, fake_input):
    fake_random([50])
    fake_input([51, 50])

    student.player_guesses_ai_number()

    actual_output = read_stdout()
    expected_output = [
        'Lower!',
        'You guessed my number!',
    ]
    assert expected_output == actual_output


def test_player_guesses_ai_number3(read_stdout, fake_random, fake_input):
    fake_random([49])
    fake_input([50, 25, 40, 49])

    student.player_guesses_ai_number()

    actual_output = read_stdout()
    expected_output = [
        'Lower!',
        'Higher!',
        'Higher!',
        'You guessed my number!',
    ]
    assert expected_output == actual_output