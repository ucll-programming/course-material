import random


def pick_random_number():
    return random.randint(1, 100)


def ask_for_number():
    return int(input("Guess my number: "))


def ask_for_feedback(guess):
    while True:
        feedback = input(f"My guess is {guess}. Is it lower, higher or correct? ").lower()
        if feedback == 'lower':
            return -1
        if feedback == 'higher':
            return 1
        if feedback == 'correct':
            return 0
        print("I couldn't understand you")


def player_guesses_ai_number():
    ai_number = pick_random_number()
    while (player_guess := ask_for_number()) != ai_number:
        if player_guess < ai_number:
            print('Higher!')
        elif player_guess > ai_number:
            print('Lower!')

    print('You guessed my number!')


def ai_guesses_player_number():
    lower = 1
    upper = 100
    while lower <= upper:
        middle = (lower + upper) // 2
        feedback = ask_for_feedback(middle)
        if feedback == 1:
            lower = middle + 1
        if feedback == -1:
            upper = middle - 1
        if feedback == 0:
            print('I won!')
            return
    print("I think you're cheating...")


if __name__ == '__main__':
    ai_guesses_player_number()
