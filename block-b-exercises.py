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

    # Uppercase Single Character
    'A': 'А', 'B': 'Б', 'V': 'В', 'G': 'Г', 'D': 'Д',
    'E': 'Е', 'Z': 'З', 'I': 'И', 'J': 'Ж', 'K': 'К',
    'L': 'Л', 'M': 'М', 'N': 'Н', 'O': 'О', 'P': 'П',
    'R': 'Р', 'S': 'С', 'C': 'С', 'T': 'Т', 'U': 'У', 'F': 'Ф',
    'H': 'Ҳ', 'Y': 'Й', 'Q':'Қ', 'X': 'Х',

    # Lowercase Single Character
    'a': 'а', 'b': 'б', 'v': 'в', 'g': 'г', 'd': 'д',
    'e': 'е', 'z': 'з', 'i': 'и', 'j': 'й', 'k': 'к',
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

    sorted_result = sorted(result, key=lambda x: x[1], reverse=True)
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


if __name__ == "__main__":
    print(tier_9("Calom"))
