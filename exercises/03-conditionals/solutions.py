def my_abs(x):
    if x < 0:
        return -x
    return x


def sign(x):
    if x < 0:
        return -1
    if x == 0:
        return 0
    return 1


def total_cost(amount):
    if amount < 100:
        amount += 10
    if amount >= 200:
        amount *= 0.95
    return amount


def rock_paper_scissors(player1_choice, player2_choice):
    rock = 0
    paper = 1
    scissors = 2
    if player1_choice == player2_choice:
        return 0
    if player1_choice == rock and player2_choice == scissors:
        return 1
    if player1_choice == paper and player2_choice == rock:
        return 1
    if player1_choice == scissors and player2_choice == paper:
        return 1
    return 2
