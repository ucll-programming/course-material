def greet(name):
    return f"Hello, {name}!"


def interactive_greet():
    name = input("What is your name? ")
    print(greet(name))


def tip_calculator():
    total_price = int(input('Enter total price: '))
    tip_percentage = input("Enter tip percentage (default=20): ")
    if len(tip_percentage) == 0:
        tip_percentage = 20
    else:
        tip_percentage = int(tip_percentage)
    total = round(total_price * (1 + tip_percentage / 100))
    print(f'You have to pay {total}')


def mask(password):
    return "*" * len(password)


def underline(password):
    return password + "\n" + "-" * len(password)


def box(string):
    top = "+" + "-" * (len(string) + 2) + "+"
    middle = "| " + string + " |"
    bottom = top
    return f"{top}\n{middle}\n{bottom}"


def format_position(x, y):
    return f"({x}, {y})"


def parse_position_x(string):
    without_parentheses = string[1:-1]
    index = without_parentheses.find(',')
    left = without_parentheses[:index]
    return int(left)


def parse_position_y(string):
    without_parentheses = string[1:-1]
    index = without_parentheses.find(',')
    right = without_parentheses[index+2:]
    return int(right)


def is_capitalized(string):
    if len(string) == 0:
        return False

    first_char = string[0]
    remaining_chars = string[1:]
    return first_char.upper() == first_char and remaining_chars.lower() == remaining_chars
