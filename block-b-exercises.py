import re

latin_to_cyrillic = {
    # Uppercase Multi-character
    'Ch': 'Ч', 'CH': 'Ч',
    'Sh': 'Ш', 'SH': 'Ш',
    'Yu': 'Ю', 'YU': 'Ю',
    'Ya': 'Я', 'YA': 'Я',
    'Yo': 'Ё', 'YO': 'Ё',
    'Ts': 'Ц', 'TS': 'Ц',

    # Lowercase Multi-character
    'ch': 'ч',
    'sh': 'ш',
    'yu': 'ю',
    'ya': 'я',
    'yo': 'ё',
    'ts': 'ц',
    'o\'' : 'ў',
    'O\'' : 'Ў',
    'g\'' : 'ғ',
    'G\'' : 'Ғ',

    # Uppercase Single Character
    'A': 'А', 'B': 'Б', 'V': 'В', 'G': 'Г', 'D': 'Д',
    'E': 'Е', 'Z': 'З', 'I': 'И', 'J': 'Ж', 'K': 'К',
    'L': 'Л', 'M': 'М', 'N': 'Н', 'O': 'О', 'P': 'П',
    'R': 'Р', 'S': 'С', 'C': 'С', 'T': 'Т', 'U': 'У', 'F': 'Ф',
    'H': 'Ҳ', 'Y': 'Й', 'Q':'Қ', 'X': 'Х',

    # Lowercase Single Character
    'a': 'а', 'b': 'б', 'v': 'в', 'g': 'г', 'd': 'д',
    'e': 'е', 'z': 'з', 'i': 'и', 'j': 'ж', 'k': 'к',
    'l': 'л', 'm': 'м', 'n': 'н', 'o': 'о', 'p': 'п',
    'r': 'р', 's': 'с', 'c': 'с', 't': 'т', 'u': 'у', 'f': 'ф',
    'h': 'ҳ', 'y': 'й', 'q': 'қ', 'x': 'х'
}

def tier_7(text: str) -> list[str]:
    if len(text) == 0:
        return []

    words = text.split(" ")

    lower_case_words = list()

    for word in words:
        word_helper = ""
        for c in word:
            if c.isalpha():
                word_helper += c.lower()

        if len(word_helper) > 0:
            lower_case_words.append(word_helper)

    return lower_case_words

def tier_8(text: str) -> dict[str, int]:
    desired_words = list()
    words = text.split(" ")
    for word in words:
        word_helper = ""
        for c in word:
            if c.isalpha():
                word_helper += c.lower()

        if len(word_helper) > 0:
            desired_words.append(word_helper)

    result: dict[str, int] = dict()

    for w in desired_words:
        keys = result.keys()

        if w in keys:
            continue

        counter = 0
        for helper in desired_words:
            if w == helper:
                counter += 1

        result[w] = counter

    return result

def tier_8_complicated(text: str, n: int) -> list[tuple[str, int]]:
    desired_words = list()
    words = text.split(" ")
    for word in words:
        word_helper = ""
        for c in word:
            if c.isalpha():
                word_helper += c.lower()

        if len(word_helper) > 0:
            desired_words.append(word_helper)

    unique_words = list(set(desired_words))
    result: list[tuple[str, int]] = list()

    for w in unique_words:
        counter = 0
        for helper in desired_words:
            if w == helper:
                counter += 1

        result.append((w, counter))

    sorted_result = sorted(result, key=lambda x: (-1 * x[1], x[0]))
    return sorted_result[:n]

def tier_9(text: str) -> str:
    keys = latin_to_cyrillic.keys()

    multi_character = ['S', 'C', 'O', 'G', 's', 'c', 'o', 'g', 'Y', 'y', 'T', 't']

    i = 0
    result = ""
    while i < len(text):
        c = text[i]
        is_multi_character = False
        char_helper = ""
        if not c.isalpha():
            result += text[i]
            i = i + 1
            continue
        if c in keys and c not in multi_character:
            is_multi_character = False
        elif c in keys and (i+1) < len(text) and text[i+1] in ["'", "h", "H", "A", 'a', 'U', 'u', 'O', 'o', 's', 'S']:
            match c.lower():
                case "s" | "c":
                    if text[i+1].lower() == 'h':
                        is_multi_character = True
                        char_helper = c + text[i+1]
                case "o" | 'g':
                    if text[i + 1].lower() == "'":
                        is_multi_character = True
                        char_helper = c + text[i + 1]
                case "y":
                    if text[i + 1].lower() in ['a', 'u']:
                        is_multi_character = True
                        char_helper = c + text[i + 1]
                case "t":
                    if text[i + 1].lower() == 's':
                        is_multi_character = True
                        char_helper = c + text[i + 1]

        if is_multi_character:
            result += latin_to_cyrillic[char_helper]
            i = i + 2
        else:
            result += latin_to_cyrillic[c]
            i = i + 1

    return result

def tier_10(a: str, b: str) -> int:
    if len(a) != len(b):
        raise RuntimeError("string size should be equal")

    difference_count = 0

    for i in range(len(a)):
        if a[i] != b[i]:
            difference_count += 1

    return difference_count

def tier_10_complicated(a: str, b: str) -> int:
    a_word_length = len(a)
    b_word_length = len(b)
    distance_count = 0
    for i in range(b_word_length):
        if i == a_word_length - 1 or i == b_word_length - 1:
            if a_word_length > b_word_length:
                distance_count += a_word_length - b_word_length
            elif a_word_length < b_word_length:
                distance_count += b_word_length - a_word_length
            break

        if a[i] != b[i]:
            distance_count += 1

    return distance_count

def tier_11(log_lines: list[str]) -> dict[str, int]:

    log_pattern = r"^\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\s+([^\s]+)"

    result: dict[str, int] = dict()

    for log in log_lines:
        match = re.match(log_pattern, log)
        if match:
            log_info = match.group(1)
            if log_info.upper() in result:
                current_count = result[log_info.upper()]
                current_count += 1
                result[log_info.upper()] = current_count
            elif log_info.upper() not in result:
                result[log_info.upper()] = 1

    return result

def tier_12(line: str) -> list[str]:
    commas = [index for index, char in enumerate(line) if char == ","]
    quotes = [index for index, char in enumerate(line) if char == "\""]

    if len(quotes) == 0:
        return line.split(",")

    if len(commas) == 0:
        return [line[1:-1]]

    removable_comma_indexes = []
    quote_index = 0
    while True:
        quote_1 = quotes[quote_index]
        if quote_index + 1 == len(quotes):
            quote_2 = len(line) - 1
        else:
            quote_2 = quotes[quote_index + 1]

        for el in commas:
            if quote_1 < el < quote_2:
                removable_comma_indexes.append(el)

        quote_index += 2

        if quote_index >= len(quotes):
            break
    for r_ind in removable_comma_indexes:
        commas.remove(r_ind)

    if len(commas) == 0:
        return [line]

    result: list[str] = []
    index = 0
    starting_index = 0

    while True:
        comma_index = commas[index]
        value = line[starting_index:comma_index]
        if len(value) > 0 and (value[0] == "\"" and value[-1] == "\""):
            value = value[1:-1]

        result.append(value)
        starting_index = comma_index + 1
        index += 1

        if index == len(commas):
            value = line[starting_index:]
            if len(value) > 0 and (value[0] == "\"" and value[-1] == "\""):
                value = value[1:-1]

            result.append(value)
            break

    return result

def tier_13(template: str, values: dict[str, object]) -> str:
    for key, value in values.items():
        template = template.replace('{' + str(key) + '}', str(value))
    return template


if __name__ == "__main__":
    # txt = '"x",,"y"'
    # print(tier_12(txt), len(tier_12(txt)))
    # print(tier_8_complicated("cherry banana apple", 2))
    print(sorted([("the", 2), ("cat", 2), ("bird", 1)], key=lambda x: (-1*x[1], x[0])))

