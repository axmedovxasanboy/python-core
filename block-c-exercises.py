from email.base64mime import header_length
from unittest import result


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
        key_element = elem[0]
        if key_element not in helper_set:
            result[key_element] = [elem[1]]
            helper_set.add(elem[0])

        else:
            values = result[key_element]
            values.append(elem[1])
            result[key_element] = values

    return result


def tier_15_complicated(pairs: list[tuple[str, float]]) -> dict[str, float]:
    result: dict[str, float] = dict()

    values = tier_15(pairs)

    for key, value_list in values.items():
        total = 0
        for el in value_list:
            total += el

        result[key] = total / len(value_list)

    return result


def tier_16(nested: list[list[int]]) -> list[int]:
    return [num for row in nested for num in row if num % 2 == 0]


def tier_17(rows: list[list]) -> list[list]:
    result: list[list] = list()

    row_length = len(rows[0])

    for i in range(row_length):
        holder = list()

        for row in rows:
            holder.append(row[i])

        result.append(holder)

    return result


def tier_17_complicated(rows: list[list]) -> list[list]:
    return list(zip(*rows))


def tier_18(values: list[float]) -> list[float]:
    min_num = min(values)
    max_num = max(values)

    if min_num == max_num:
        raise Exception("Minimum and maximum numbers are equal")

    result: list[float] = list()

    for v in values:
        helper = (v - min_num) / (max_num - min_num)
        result.append(helper)

    return result


def tier_19(labels: list[str]) -> list[list[int]]:
    helper = set()
    unique_values = list()
    result: list[list[int]] = list()
    for l in labels:
        if l not in helper:
            unique_values.append(l)

    unique_values.sort()
    value_map = dict()

    for i, v in enumerate(unique_values):
        value_map[v] = i

    for label in labels:
        holder = list()
        for key, value in value_map.items():
            if label == key:
                holder.append(1)
            else:
                holder.append(0)
        result.append(holder)

    return result


def tier_20(items: list, k: int) -> list[list]:
    result: list[list] = list()

    holder = list()

    for i in items:
        holder.append(i)

        if len(holder) == k:
            result.append(holder)
            holder = list()


    result.append(holder)

    return result

def tier_21(a: dict[int, float], b: dict[int, float]) -> float:
    pass


if __name__ == "__main__":
    # print(tier_17([[1, 5], [2, 6], [3, 7], [4, 8]]))

    print(tier_20([1, 2, 3, 4, 5], 2))
