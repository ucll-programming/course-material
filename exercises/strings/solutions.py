def greet(name):
    return f"Hello, {name}!"


def interactive_greet():
    name = input("What is your name? ")
    print(greet(name))


def tip_calculator():
    total_price = int(input('Enter total price: '))
    tip_percentage = input("Enter tip percentage (default=20): ")
    if tip_percentage == "":
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
    return f"({x:.3f}, {y:.3f})"


def parse_position_x(string):
    without_parentheses = string[1:-1]
    index = without_parentheses.find(',')
    left = without_parentheses[:index]
    return float(left)


def parse_position_y(string):
    without_parentheses = string[1:-1]
    index = without_parentheses.find(',')
    right = without_parentheses[index+2:]
    return float(right)


def is_capitalized(string):
    if len(string) == 0:
        return False

    first_char = string[0]
    remaining_chars = string[1:]
    return first_char.upper() == first_char and remaining_chars.lower() == remaining_chars


def is_digit(char):
    return char in '0123456789'


def is_student_id(string):
    if len(string) != 8:
        return False
    if string[0].lower() not in 'rs':
        return False
    if not is_digit(string[1]):
        return False
    if not is_digit(string[2]):
        return False
    if not is_digit(string[3]):
        return False
    if not is_digit(string[4]):
        return False
    if not is_digit(string[5]):
        return False
    if not is_digit(string[6]):
        return False
    if not is_digit(string[7]):
        return False
    return True


def palindrome(string):
    return string == string[::-1]


def parse_day(string):
    return int(string[:2])


def parse_month(string):
    return int(string[3:5])


def parse_year(string):
    return int(string[6:])


def fix_date(string):
    month = string[:2]
    day = string[3:5]
    year = string[6:]
    return f'{year}/{month}/{day}'


def last_character(string):
    if len(string) != 0:
        return string[len(string) - 1]
    else:
        return None
