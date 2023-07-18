def multiple_choice(right_answer, given_answer):
    if right_answer == given_answer:
        return 1
    elif given_answer is None:
        return 0
    else:
        return -0.2
