def delete_nth(order: list[int], max_e: int) -> list[int]:
    counter = {}
    result = []
    for num in order:
        if num not in counter:
            counter[num] = 0
        if counter[num] < max_e:
            result.append(num)
            counter[num] += 1
    return result
