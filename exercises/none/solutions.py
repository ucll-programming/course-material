def multiple_choice(right_answer, given_answer):
    if right_answer == given_answer:
        return 1
    elif given_answer is None:
        return 0
    else:
        return -0.2


def entrance_exam(grade1, grade2, grade3, grade4, grade5):
    n_skipped = 0
    n_taken = 0
    total = 0

    if grade1 is None:
        n_skipped += 1
    else:
        n_taken += 1
        total += grade1

    if grade2 is None:
        n_skipped += 1
    else:
        n_taken += 1
        total += grade2

    if grade3 is None:
        n_skipped += 1
    else:
        n_taken += 1
        total += grade3

    if grade4 is None:
        n_skipped += 1
    else:
        n_taken += 1
        total += grade4

    if grade5 is None:
        n_skipped += 1
    else:
        n_taken += 1
        total += grade5

    if n_skipped > 1:
        return False
    if total / n_taken < 12:
        return False

    return True
