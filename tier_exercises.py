from enum import Enum

class CheckStyle(Enum):
    NATURAL_NUMBERS = 1 # 1, 2, 3, ...
    WHOLE_NUMBERS = 2 # 0, 1, 2, 3 ...
    INTEGER_NUMBERS = 3 # ... -3, -2, -1, 0, 1, 2, 3 ...
    RATIONAL_NUMBERS = 4 # fraction of two integers
    POSITIVE_RATIONALS = 7 # >= 0
    NEGATIVE_INTEGERS = 6 # < 0
    NEGATIVE_RATIONALS = 8 # < 0


def is_valid_number(n: str, check_style: CheckStyle) -> bool | None:

    has_dot = False
    has_minus_sign = has_plus_sign = False

    for i in range(len(n)):
        if i == 0:
            if n[i] == "-":
                has_minus_sign = True
            elif n[i] == "+":
                has_plus_sign = True

        if n[i] == ".":
            if not has_dot:
                has_dot = True
            else: 
                return False
        elif n[i] == ",":
            return False
        elif i != 0 and (n[i] == '+' or n[i] == '-'):
            return False

    match check_style:
        case CheckStyle.NATURAL_NUMBERS:
            try:
                if not has_dot and not has_minus_sign:
                    num = int(n)
                    if num >= 1:
                        return True
            except ValueError as e:
                print(e)
                return False

        case CheckStyle.WHOLE_NUMBERS:
            try:
                if not has_dot and not has_minus_sign:
                    num = int(n)
                    if num >= 0:
                        return True
            except ValueError as e:
                print(e)
                return False

        case CheckStyle.INTEGER_NUMBERS:
            try:
                if not has_dot:
                    int(n)
                    return True
            except ValueError as e:
                print(e)
                return False
        case CheckStyle.RATIONAL_NUMBERS:
            try:
                if has_dot:
                    float(n)
                    return True
            except ValueError as e:
                print(e)
                return False
        case CheckStyle.POSITIVE_RATIONALS:
            try:
                if not has_minus_sign:
                    float(n)
                    return True
            except ValueError as e:
                print(e)
                return False



def tier_1():

    print("Tier 0. Block A — Control flow & numbers (1–6)")

    print("""
    1. Confidence bucketer ● · loops, conditionals, counting
    Given a list of model confidence scores (floats 0–1), classify each as "low" (<0.4), "mid" (<0.8), or "high", and return how many fell in each bucket.
    [0.91, 0.2, 0.55, 0.99] → {"low": 1, "mid": 1, "high": 2}
    """)

    low_threshold = 0.4
    mid_threshold = 0.8
    high_threshold = 1

    numbers = list()

    print("Program is started. For stopping use one of these: q / exit / quit")

    user_input = input("You can enter any number we will add <0.> to the given number\nEnter your number: 0.").lower().strip()

    while user_input != "q" and user_input != "exit" and user_input != "quit":

        break

def tier_2():
    pass
def tier_3():
    pass