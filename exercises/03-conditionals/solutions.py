from math import ceil


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
    elif player1_choice == rock and player2_choice == scissors:
        return 1
    elif player1_choice == paper and player2_choice == rock:
        return 1
    elif player1_choice == scissors and player2_choice == paper:
        return 1
    else:
        return 2


def player_movement(position, left_arrow, right_arrow, shift):
    if shift:
        step = 2
    else:
        step = 1

    if left_arrow:
        position -= step
    if right_arrow:
        position += step

    return position


def movie_ticket(duration, imax, student, ticket_count):
    if duration <= 90:
        cost = 10
    elif duration <= 120:
        cost = 11
    elif duration <= 150:
        cost = 12
    else:
        cost = 15

    if imax:
        cost = ceil(cost * 1.2)

    if student:
        cost -= 3

    return cost * ticket_count
