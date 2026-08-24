from enum import Enum
from typing import Optional


class CheckStyle(Enum):
    NATURAL_NUMBERS = 1 # 1, 2, 3, ...
    WHOLE_NUMBERS = 2 # 0, 1, 2, 3 ...
    INTEGER_NUMBERS = 3 # ... -3, -2, -1, 0, 1, 2, 3 ...
    RATIONAL_NUMBERS = 4 # fraction of two integers
    POSITIVE_RATIONALS = 7 # >= 0 (fraction of two positive integers)
    NEGATIVE_INTEGERS = 6 # < 0 (-1, -2, -3, -4, ...)
    NEGATIVE_RATIONALS = 8 # < 0 (fraction of two integers and result is negative)
    ANY_NUMBER = 9 # ... -3.0, -2.9, -1.98, -0.97, 0, 1.1, 2.2, 3.3, 4.4 ...

class ValidNumber:

    class NumberType(Enum):
        INTEGER = 0
        RATIONAL = 1

    user_number: str
    is_valid: bool = False
    number_type: Optional[NumberType]
    valid_number: Optional[int | float]

    def __init__(self, user_number: str):
        self.user_number = user_number
        self.is_valid = False
        self.number_type = None
        self.valid_number = None


def is_valid_number(n: str, check_style: CheckStyle) -> ValidNumber:

    has_dot = False
    has_minus_sign = has_plus_sign = False

    valid = ValidNumber(n)


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
                return valid
        elif n[i] == ",":
            return valid
        elif i != 0 and (n[i] == '+' or n[i] == '-'):
            return valid

    match check_style:
        case CheckStyle.NATURAL_NUMBERS:
            valid.is_valid = False
            try:
                if not has_dot and not has_minus_sign:
                    num = int(n)
                    if num >= 1:
                        valid.is_valid = True
                        valid.number_type = ValidNumber.NumberType.INTEGER
                        valid.valid_number = num
                        return valid
                return valid
            except ValueError as e:
                print(e)
                return valid

        case CheckStyle.WHOLE_NUMBERS:
            valid.is_valid = False
            try:
                if not has_dot and not has_minus_sign:
                    num = int(n)
                    if num >= 0:
                        valid.is_valid = True
                        valid.number_type = ValidNumber.NumberType.INTEGER
                        valid.valid_number = num
                        return valid
                return valid
            except ValueError as e:
                print(e)
                return valid

        case CheckStyle.INTEGER_NUMBERS:
            valid.is_valid = False
            try:
                if not has_dot:
                    num = int(n)
                    valid.is_valid = True
                    valid.number_type = ValidNumber.NumberType.INTEGER
                    valid.valid_number = num
                    return valid
                return valid
            except ValueError as e:
                print(e)
                return valid


        case CheckStyle.RATIONAL_NUMBERS:
            valid.is_valid = False
            try:
                if has_dot:
                    num = float(n)
                    valid.is_valid = True
                    valid.number_type = ValidNumber.NumberType.RATIONAL
                    valid.valid_number = num
                    return valid
                return valid
            except ValueError as e:
                print(e)
                return valid

        case CheckStyle.POSITIVE_RATIONALS:
            valid.is_valid = False
            try:
                if not has_minus_sign:
                    num = float(n)
                    if num >= 0.0:
                        valid.is_valid = True
                        valid.number_type = ValidNumber.NumberType.RATIONAL
                        valid.valid_number = num
                        return valid
                return valid
            except ValueError as e:
                print(e)
                return valid

        case CheckStyle.NEGATIVE_INTEGERS:
            valid.is_valid = False
            try:
                if not has_plus_sign and has_minus_sign and not has_dot:
                    num = int(n)
                    if num < 0:
                        valid.is_valid = True
                        valid.number_type = ValidNumber.NumberType.INTEGER
                        valid.valid_number = num
                        return valid
                return valid
            except ValueError as e:
                print(e)
                return valid

        case CheckStyle.NEGATIVE_RATIONALS:
            valid.is_valid = False
            try:
                if has_minus_sign and not has_plus_sign and has_dot:
                    num = float(n)
                    if num < 0:
                        valid.is_valid = True
                        valid.valid_number = num
                        valid.number_type = ValidNumber.NumberType.RATIONAL
                        return valid
                return valid
            except ValueError as e:
                print(e)
                return valid

        case CheckStyle.ANY_NUMBER:
            valid.is_valid = False
            try:
                num = float(n)
                valid.is_valid = True
                valid.valid_number = num
                valid.number_type = ValidNumber.NumberType.RATIONAL
                return valid
            except ValueError as e:
                print(e)
                return valid

def exercise_1():

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
        number = is_valid_number(user_input, check_style=CheckStyle.NATURAL_NUMBERS)
        if number.is_valid:
            if number.valid_number is None:
                raise Exception("Please enter a valid number")
            else:
                num_length = len(str(number.valid_number))
                desired_number = number.valid_number / (10 ** num_length)
                numbers.append(desired_number)
        else:
            print("Please enter a valid number. Do not add any dot or signs to your number.")

        user_input = input("Enter: 0.").lower().strip()


    separating_dict = dict()

    separating_dict['low_threshold'] = list()
    separating_dict['mid_threshold'] = list()
    separating_dict['high_threshold'] = list()

    for n in numbers:
        if n <= low_threshold:
            separating_dict['low_threshold'].append(n)
        elif mid_threshold >= n > low_threshold:
            separating_dict['mid_threshold'].append(n)
        elif high_threshold >= n > mid_threshold:
            separating_dict['high_threshold'].append(n)

    for item in separating_dict.keys():
        separating_dict[item] = separating_dict[item]

    for item in separating_dict.keys():
        print(item, separating_dict[item], len(separating_dict[item]))

def exercise_2():
    print("Tier 0. Block A — Control flow & numbers (1–6)")

    print("""
        2. Summary stats, by hand ●● · accumulation, comparison · 
        ⊕ Given a list of numbers, return its minimum, maximum, and mean — without min(), max(), or sum(). 
        Use a loop and understand what those built-ins do for you
        """)

    numbers = list()
    print("Program is started. For stopping use one of these: q / exit / quit")

    user_input = input("Please enter any number you want.\n>>> ").lower().strip()

    while user_input != "q" and user_input != "exit" and user_input != "quit":
        valid_number = is_valid_number(user_input, check_style=CheckStyle.ANY_NUMBER)
        if valid_number.is_valid:
            if valid_number.valid_number is None:
                raise Exception("Please enter a valid number")

            numbers.append(valid_number.valid_number)
        else:
            print("Please enter a valid number")

        user_input = input(">>> ").lower().strip()

    min_num = numbers[0]
    max_num = numbers[0]
    total = 0

    for item in numbers:
        if item < min_num:
            min_num = item
        if item > max_num:
            max_num = item
        total += item

    print("Numbers: ", numbers)
    print("Minimum number: ", min_num)
    print("Maximum number: ", max_num)
    print("Mean: ", total/len(numbers))

def exercise_2_complicated():
    print("Tier 0. Block A — Control flow & numbers (1–6)")

    print("Now you may use the built-ins — and also return the median, which has no single built-in (sort, then handle even vs odd length).")

    numbers = list()
    print("Program is started. For stopping use one of these: q / exit / quit")

    user_input = input("Please enter any number you want.\n>>> ").lower().strip()

    while user_input != "q" and user_input != "exit" and user_input != "quit":
        valid_number = is_valid_number(user_input, check_style=CheckStyle.ANY_NUMBER)
        if valid_number.is_valid:
            if valid_number.valid_number is None:
                raise Exception("Please enter a valid number")

            numbers.append(valid_number.valid_number)
        else:
            print("Please enter a valid number")

        user_input = input(">>> ").lower().strip()

    min_num = min(numbers)
    max_num = max(numbers)
    total = sum(numbers)
    mean = total/len(numbers)
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    medians = list()
    if length % 2 == 0:
        medians = [sorted_numbers[length // 2 - 1], sorted_numbers[length // 2]]
    else:
        medians = [sorted_numbers[length // 2]]

    print("Numbers: ", numbers)
    print("Minimum: ", min_num)
    print("Maximum: ", max_num)
    print("Mean: ", mean)
    print("Sorted numbers: ", sorted_numbers)
    print("Median(s): ", medians)

def exercise_3():
    print("Tier 0. Block A — Control flow & numbers (1–6)")

    print("3. Longest streak ●●● ★ · "
          "stateful iteration Given a list of daily values and a threshold, find the length of the longest consecutive run where the value stayed strictly above the threshold. "
          "(This is your MVD streak logic, and anomaly-streak detection.) [1, 5, 6, 2, 7, 8, 9, 1], threshold=4 → 3 (the run 7,8,9) "
          "Trap: you need to track \"current run\" and \"best run so far\" separately, and reset at the right moment.")

    total_numbers = list()
    threshold_above_numbers = list()
    desired_threshold = list()
    print("Program is started. For stopping use one of these: q / exit / quit")

    threshold = input("Please enter a number you want to be a threshold.\n>>> ").lower().strip()
    countdown = 0
    best = 0

    while threshold != "q" and threshold != "exit" and threshold != "quit":
        valid_number = is_valid_number(threshold, check_style=CheckStyle.ANY_NUMBER)
        if valid_number.is_valid:
            if valid_number.valid_number is None:
                raise Exception("Please enter a valid number")
            threshold = valid_number.valid_number
            break

    user_input = input("Please enter any number you want.\n>>> ").lower().strip()

    while user_input != "q" and user_input != "exit" and user_input != "quit":
        valid_number = is_valid_number(user_input, check_style=CheckStyle.ANY_NUMBER)
        if valid_number.is_valid:
            valid_num = valid_number.valid_number
            if valid_num is None:
                raise Exception("Please enter a valid number")

            if valid_num >= threshold:
                threshold_above_numbers.append(valid_num)
                countdown += 1
            elif valid_num < threshold:
                if best < countdown:
                    best = countdown
                if len(threshold_above_numbers) > len(desired_threshold):
                    desired_threshold = threshold_above_numbers.copy()

                countdown = 0
                threshold_above_numbers = list()

            total_numbers.append(valid_number.valid_number)
        else:
            print("Please enter a valid number")

        user_input = input(">>> ").lower().strip()


    print("Total number list: ", total_numbers)
    print("Selected threshold: ", threshold)
    print("Numbers above threshold: ", desired_threshold)
    print("The best threshold numbers so far: ", best)

def exercise_4():
    print("Tier 0. Block A — Control flow & numbers (1–6)")

    print("4. ID checksum validator ●●● · indexing, modular arithmetic · →fraud (#6)\n"
          "Validate a number string by a check-digit rule: double every second digit from the right;\n"
          "if doubling gives a two-digit number, sum its digits;\n"
          "total all digits;\n"
          "the string is valid iff the total is divisible by 10. \n"
          "(This is the Luhn algorithm — it's what's behind Uzcard/Humo/Visa number validation.) \"4561261212345467\" → True \n"
          "Trap: \"from the right\" and the doubling-then-digit-sum step are where it breaks.")

    user_input = input("Please enter any number you want Recommended length of number is 8.\n>>> ").lower().strip()

    valid_number = is_valid_number(user_input, check_style=CheckStyle.NATURAL_NUMBERS)
    if valid_number.is_valid:
        if valid_number.valid_number is None:
            raise Exception("Please enter a valid number")

        if len(user_input) < 8:
            print("you have entered less than recommended length")
    else:
        print("Please enter a valid number")
        return

    user_num = valid_number.user_number
    print(user_num)

    for i in range(len(user_num)-1, -1, -1):
        if (i+1) % 2 == 0:
            helper = int(user_num[i])
            helper = helper * 2


        print(user_num[i])

def exercise_5():
    print("Tier 0. Block A — Control flow & numbers (1–6)")

    print("""
            5. Human-readable units ●● · integer division, modulo, formatting 
            Write two converters: bytes → a string like "2.4 MB" (use 1024 steps: B, KB, MB, GB), 
            and seconds → "2h 15m 30s" (drop zero parts: 90 → "1m 30s"). 
            You'll format latency and throughput like this constantly.
            """)

    print("Program is started. For stopping use one of these: q / exit / quit")

    unit_type = input("""
        Please select unit type.
        0. File size (Bytes -> KB, MB, GB, TB, etc.)
        1. Seconds (Seconds -> Minutes, Hours, etc.)
        >>> """)
    valid_unit_type = is_valid_number(unit_type, check_style=CheckStyle.WHOLE_NUMBERS)
    if not valid_unit_type.is_valid:
        print("Please enter a valid unit type")
        raise ValueError("Invalid number provided")
    unit = valid_unit_type.valid_number


    user_unit = input("Please enter any unit you want.\n>>> ").lower().strip()

    valid_user_input = is_valid_number(user_unit, check_style=CheckStyle.WHOLE_NUMBERS)

    if not valid_user_input.is_valid:
        print("Please enter a valid unit number")
        raise ValueError("Invalid number provided")

    unit_number = valid_user_input.valid_number
    if unit_number is None or unit_number == "":
        raise ValueError("Valid number not found")

    if 0 == unit or 1 == unit:
        unit_type = unit
    else:
        raise ValueError("Invalid unit provided")

    if unit_type == 0:
        unit_identifier = 0
        helper = int(unit_number)
        while helper >= 1024:
            helper = float(helper / 1024)
            unit_identifier += 1

        if unit_identifier == 0: # bytes
            print(f"{unit_number} Bytes")
        elif unit_identifier == 1: # KB
            print(f"{unit_number} Bytes -> {helper:.2f} Kb")
        elif unit_identifier == 2: # MB
            print(f"{unit_number} Bytes -> {helper:.2f} MB")
        elif unit_identifier == 3: # GB
            print(f"{unit_number} Bytes -> {helper:.2f} GB")
        elif unit_identifier == 4: # TB
            print(f"{unit_number} Bytes -> {helper:.2f} TB")
        else:
            raise ValueError("Unrecognized error have been occurred")


    elif unit_type == 1:
        unit_identifier = 0
        helper = int(unit_number)
        centuries = years = days = hours = minutes = seconds = None
        while helper >= 10:

            if unit_identifier == 0:
                seconds = int(helper) % 60
                helper = float(helper / 60)
                minutes = int(helper)
                unit_identifier += 1
            elif unit_identifier == 1:
                minutes = int(helper) % 60
                helper = float(helper / 60)
                hours = int(helper)
                unit_identifier += 1
            elif unit_identifier == 2:
                hours = int(helper) % 24
                helper = float(helper / 24)
                days = int(helper)
                unit_identifier += 1
            elif unit_identifier == 3 and helper > 365:
                days = int(helper) % 365
                helper = float(helper / 365)
                years = int(helper)
                unit_identifier += 1
            elif unit_identifier == 4 and helper >= 100:
                years = int(helper) % 100
                helper = float(helper / 100)
                centuries = int(helper)
                unit_identifier += 1
            else:
                break

        if unit_identifier == 0:
            print(f"{unit_number} Seconds")
        elif unit_identifier == 1:
            print(f"{unit_number} Seconds -> {helper:.2f} Minutes")
        elif unit_identifier == 2:
            print(f"{unit_number} seconds -> {hours} Hours {minutes} Minutes {seconds} Seconds")
        elif unit_identifier == 3:
            print(f"{unit_number} Seconds -> {days} Days {hours} Hours {minutes} Minutes {seconds} Seconds")
        elif unit_identifier == 4:
            print(f"{unit_number} Seconds -> {years} Years {days} Days {hours} Hours {minutes} Minutes {seconds} Seconds")
        elif unit_identifier == 5:
            print(f"{unit_number} Seconds -> {centuries} Centuries {years} Years {days} Days {hours} Hours {minutes} Minutes {seconds} Seconds ")

    else:
        raise ValueError("Unrecognized error have been occurred")


if __name__ == "__main__":
    exercise_5()