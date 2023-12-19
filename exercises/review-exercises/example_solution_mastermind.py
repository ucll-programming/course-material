def mastermind(code, guess):
    checked_code = code.copy()
    correct = 0
    wrong_pos = 0
    for i in range(len(checked_code)):
        if checked_code[i] == guess[i]:
            correct += 1
            checked_code[i] = 'c'
        elif guess[i] in checked_code:
            wrong_pos += 1
    return [correct,wrong_pos]