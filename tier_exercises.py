import math
from enum import Enum
from typing import Optional


class CheckStyle(Enum):
    NATURAL_NUMBERS = 1  # 1, 2, 3, ...
    WHOLE_NUMBERS = 2  # 0, 1, 2, 3 ...
    INTEGER_NUMBERS = 3  # ... -3, -2, -1, 0, 1, 2, 3 ...
    RATIONAL_NUMBERS = 4  # fraction of two integers
    POSITIVE_RATIONALS = 7  # >= 0 (fraction of two positive integers)
    NEGATIVE_INTEGERS = 6  # < 0 (-1, -2, -3, -4, ...)
    NEGATIVE_RATIONALS = 8  # < 0 (fraction of two integers and result is negative)
    ANY_NUMBER = 9  # ... -3.0, -2.9, -1.98, -0.97, 0, 1.1, 2.2, 3.3, 4.4 ...


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
    n = n.replace(",", ".")

    has_dot = False
    has_minus_sign = has_plus_sign = False

    valid = ValidNumber(n)
    if len(n.strip()) == 0:
        valid.is_valid = False
        return valid

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


def tier_1(scores: list[float]) -> dict[str, int]:
    low_threshold = 0.4
    mid_threshold = 0.8

    separating_dict = dict()

    separating_dict['low'] = list()
    separating_dict['mid'] = list()
    separating_dict['high'] = list()

    result = dict()

    for n in scores:
        if n < low_threshold:
            separating_dict['low'].append(n)
        elif n < mid_threshold:
            separating_dict['mid'].append(n)
        elif n >= mid_threshold:
            separating_dict['high'].append(n)

    for item in separating_dict.keys():
        result[item] = len(separating_dict[item])

    return result


def tier_1_optimal(scores: list[float]) -> dict[str, int]:
    counts = {"low": 0, "mid": 0, "high": 0}
    for score in scores:
        if score < 0.4:
            counts["low"] += 1
        elif score < 0.8:
            counts["mid"] += 1
        else:
            counts["high"] += 1
    return counts


def tier_2(numbers: list[float]) -> tuple[float, float, float] | None:
    if len(numbers) == 0:
        return None
    min_num = numbers[0]
    max_num = numbers[0]
    total = 0

    for item in numbers:
        if item < min_num:
            min_num = item
        if item > max_num:
            max_num = item
        total += item

    return min_num, max_num, total / len(numbers)


def tier_2_complicated(numbers: list[float]) -> tuple[float, float, float, float] | None:
    if len(numbers) == 0:
        return None
    min_num = min(numbers)
    max_num = max(numbers)
    total = sum(numbers)
    mean = total / len(numbers)
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    medians = list()
    if length % 2 == 0:
        medians = [sorted_numbers[length // 2 - 1], sorted_numbers[length // 2]]
    else:
        medians = [sorted_numbers[length // 2]]

    median = 0

    for m in medians:
        median += m

    if len(medians) > 1:
        median = median / 2

    return min_num, max_num, mean, median


def tier_2_complicated_optimal(numbers: list[float]) -> tuple[float, float, float, float]:
    if not numbers:
        raise ValueError("tier_2_complicated_optimal() needs at least one number")

    ordered = sorted(numbers)
    n = len(ordered)
    mid = n // 2
    if n % 2 == 1:
        median = ordered[mid]
    else:
        median = (ordered[mid - 1] + ordered[mid]) / 2

    return ordered[0], ordered[-1], sum(ordered) / n, median


def tier_3(values: list[float], threshold: float) -> int:
    countdown = 0
    best = 0

    for v in values:
        if v > threshold:
            countdown += 1
        elif v <= threshold:
            countdown = 0

        if best < countdown:
            best = countdown
    return best


def tier_3_optimal(values: list[float], threshold: float) -> int:
    current = best = 0
    for v in values:
        if v > threshold:
            current += 1
            if current > best:
                best = current
        else:
            current = 0
    return best


def tier_4(number: str) -> bool:
    untouched_numbers = list()
    multiplied_numbers = list()

    num_length = len(number)
    for i in range(0, num_length):

        position_from_right = num_length - i

        if position_from_right % 2 == 0:
            multiplied = int(number[i]) * 2
            multiplied_num = 0
            if multiplied >= 10:
                while multiplied != 0:
                    multiplied_num += multiplied % 10
                    multiplied = int(multiplied / 10)
            else:
                multiplied_num = multiplied
            multiplied_numbers.append(multiplied_num)
        else:
            untouched_numbers.append(int(number[i]))

    total = sum(multiplied_numbers) + sum(untouched_numbers)

    return total % 10 == 0


def tier_4_optimal(number: str) -> bool:
    if len(number) < 2 or not number.isdigit():
        return False

    total = 0
    for i, ch in enumerate(reversed(number)):
        digit = int(ch)
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit
    return total % 10 == 0


def tier_5_bytes(n: int) -> str:
    unit_identifier = 0
    helper = n
    while helper >= 1024:
        helper = float(helper / 1024)
        unit_identifier += 1

    if unit_identifier == 0:  # bytes
        return f"{n} Bytes"
    elif unit_identifier == 1:  # KB
        return f"{helper:.2f} Kb"
    elif unit_identifier == 2:  # MB
        return f"{helper:.2f} MB"
    elif unit_identifier == 3:  # GB
        return f"{helper:.2f} GB"
    elif unit_identifier == 4:  # TB
        return f"{helper:.2f} TB"
    else:
        raise ValueError("Unrecognized error have been occurred")


def tier_5_bytes_optimal(n: int) -> str:
    if n < 0:
        raise ValueError(f"byte count can't be negative: {n}")
    units = ["B", "KB", "MB", "GB", "TB"]
    size = n
    for unit in units:
        if round(size, 2) < 1024 or unit == units[-1]:
            return f"{n} B" if unit == "B" else f"{size:.2f} {unit}"
        size /= 1024


def tier_5_seconds(n: int) -> str:
    unit_identifier = 0
    helper = n
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
    result = ""

    if unit_identifier == 0:
        return f"{n}s"
    elif unit_identifier == 1:
        if minutes > 0:
            result += f"{minutes}m "

        if seconds > 0:
            result += f"{seconds}s"

        return result.strip()

    elif unit_identifier == 2:
        if hours > 0:
            result += f"{hours}h "

        if minutes > 0:
            result += f"{minutes}m "

        if seconds > 0:
            result += f"{seconds}s"

        return result.strip()

    elif unit_identifier == 3:
        if days > 0:
            result += f"{days}d "
        if hours > 0:
            result += f"{hours}h "
        if minutes > 0:
            result += f"{minutes}m "
        if seconds > 0:
            result += f"{seconds}s"

        return result.strip()

    elif unit_identifier == 4:
        if years > 0:
            result += f"{years}y "
        if days > 0:
            result += f"{days}d "
        if hours > 0:
            result += f"{hours}h "
        if minutes > 0:
            result += f"{minutes}m "
        if seconds > 0:
            result += f"{seconds}s"

        return result.strip()

    elif unit_identifier == 5:
        if centuries > 0:
            result += f"{centuries}c "
        if years > 0:
            result += f"{years}y "
        if days > 0:
            result += f"{days}d "
        if hours > 0:
            result += f"{hours}h "
        if minutes > 0:
            result += f"{minutes}m "
        if seconds > 0:
            result += f"{seconds}s"

        return result.strip()
    else:
        raise ValueError("Unrecognized error have been occurred")


def tier_5_seconds_optimal(n: int) -> str:
    if n < 0:
        raise ValueError(f"duration can't be negative: {n}")
    if n == 0:
        return "0s"
    parts = []
    remaining = n
    for suffix, size in (("d", 86400), ("h", 3600), ("m", 60), ("s", 1)):
        count, remaining = divmod(remaining, size)
        if count:
            parts.append(f"{count}{suffix}")
    return " ".join(parts)


def tier_6_parse(raw: str) -> float | None:
    valid_number_ = is_valid_number(raw, check_style=CheckStyle.ANY_NUMBER)
    if valid_number_.is_valid:
        return valid_number_.valid_number
    return None


def tier_6_parse_optimal(raw: str) -> float | None:
    try:
        value = float(raw)
    except ValueError:
        return None
    if not math.isfinite(value):
        return None
    return value


def tier_6() -> float | None:
    print("Program is started. For stopping use one of these: q / exit / quit")

    number_list = list()
    user_input = input("Please enter any number you want.\n>>> ").lower().strip()

    while user_input != "q" and user_input != "exit" and user_input != "quit":
        valid_number_ = is_valid_number(user_input, check_style=CheckStyle.ANY_NUMBER)

        if valid_number_.is_valid:
            number_list.append(valid_number_.valid_number)
        else:
            print("Please enter a valid number.")

        user_input = input(">>> ").lower().strip()

    if len(number_list) == 0:
        return 0
    mean = sum(number_list) / len(number_list)
    print("Mean: ", mean)
    return mean


STOP_WORDS = {"q", "exit", "quit"}


def tier_6_optimal() -> float | None:
    print("Enter numbers one per line. Stop with q / exit / quit.")
    total = 0.0
    count = 0
    while True:
        try:
            raw = input(">>> ").strip()
        except EOFError:
            break
        if raw.lower() in STOP_WORDS:
            break
        value = tier_6_parse(raw)
        if value is None:
            print(f"Not a number: {raw!r}")
            continue
        total += value
        count += 1

    if count == 0:
        print("No numbers entered.")
        return None
    mean = total / count
    print(f"Mean: {mean}")
    return mean


def tier_6_complicated_parse(raw: str) -> float | None:
    valid_number_ = is_valid_number(raw, check_style=CheckStyle.ANY_NUMBER)
    if valid_number_.is_valid:
        return valid_number_.valid_number
    return None


def tier_6_complicated_parse_optimal(raw: str) -> float | None:
    return tier_6_parse_optimal(raw.replace(",", "."))


def tier_6_complicated() -> float | None:
    print("Program is started. For stopping use one of these: q / exit / quit")

    number_list = list()
    user_input = input("Please enter any number you want.\n>>> ").lower().strip()

    while user_input != "q" and user_input != "exit" and user_input != "quit":
        valid_number_ = is_valid_number(user_input, check_style=CheckStyle.ANY_NUMBER)

        if valid_number_.is_valid:
            number_list.append(valid_number_.valid_number)
        else:
            print("Please enter a valid number.")

        user_input = input(">>> ").lower().strip()
    if len(number_list) == 0:
        return 0
    mean = sum(number_list) / len(number_list)
    print("Mean: ", mean)
    return mean


if __name__ == "__main__":
    pass
