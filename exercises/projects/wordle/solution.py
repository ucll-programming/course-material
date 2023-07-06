from collections import Counter


def judge(actual: str, guess: str) -> str:
    if len(actual) != len(guess):
        raise ValueError("actual and guess must be strings of equal length")
    length = len(actual)
    result = ["X"] * length
    counts = Counter(actual)

    for i in range(length):
        if actual[i] == guess[i]:
            result[i] = "C"
            counts[actual[i]] -= 1

    for i in range(length):
        letter = guess[i]
        if counts.get(letter, 0) > 0 and result[i] != "C":
            result[i] = "M"
            counts[letter] -= 1

    return "".join(result)
