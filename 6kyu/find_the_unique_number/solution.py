def find_uniq(arr: list[float]) -> float | None:
    counter = {}
    for num in arr:
        if num in counter:
            counter[num] += 1
        else:
            counter[num] = 1
    for num, count in counter.items():
        if count == 1:
            return num
    return None
