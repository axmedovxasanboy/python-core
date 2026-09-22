def tier_14(items: list) -> list:
    helper_set = set()
    result = []

    for el in items:
        if el not in helper_set:
            helper_set.add(el)
            result.append(el)

    return result

def tier_14_complicated(records: list[dict], key: str) -> list[dict]:
    helper_set = set()
    result = []
    for record in records:
        if record[key] not in helper_set:
            helper_set.add(record[key])
            result.append(record)

    return result

def tier_15(pairs: list[tuple[str, float]]) -> dict[str, list[float]]:
    result: dict[str, list[float]] = dict()
    helper_set = set()


    for elem in pairs:
        if elem[0] not in helper_set:
            helper_set.add(elem[0])
            helper = {elem[0]: [elem[1]]}
        else:
             result[elem[0]]



    return result


if __name__ == "__main__":
    # print(tier_14_complicated([{"id": 1, "n": "a"}, {"id": 2, "n": "b"}, {"id": 1, "n": "c"}], "id"))

    test_case: list[tuple[str, float]] = [("a", 1), ("b", 2), ("a", 3)]

    for el in test_case:
        print(el[0], list(el[1]))

