from collections import Counter
from enum import Enum


class Judgement(Enum):
    CORRECT = 0
    MISPLACED = 1
    WRONG = 2


def judge(actual: str, guess: str) -> list[Judgement]:
    if len(actual) != len(guess):
        raise ValueError("actual and guess must be strings of equal length")

    length = len(actual)
    result = [Judgement.WRONG] * length
    counts = Counter(actual)

    for i in range(length):
        if actual[i] == guess[i]:
            result[i] = Judgement.CORRECT
            counts[actual[i]] -= 1

    for i in range(length):
        letter = guess[i]
        if counts.get(letter, 0) > 0 and result[i] != Judgement.CORRECT:
            result[i] = Judgement.MISPLACED
            counts[letter] -= 1

    return result
