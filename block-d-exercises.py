def tier_22(path: str) -> tuple[int, int, int]:
    with open(path, "r", encoding="utf-8") as file:
        all_text = file.read()
        if len(all_text) == 0:
            return 0, 0 , 0
        word_count = len(all_text.split())

        if all_text.endswith("\n"):
            lines_count = all_text.count("\n")
        else:
            lines_count = all_text.count("\n") + 1

        chars_count = len(all_text)

    return lines_count, word_count, chars_count


if __name__ == '__main__':
    print(tier_22('fixtures/wc.txt'))