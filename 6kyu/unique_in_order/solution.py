def unique_in_order(sequence: str | list | tuple) -> list[int] | list[str] | None :
    result = []

    for i in range(len(sequence)):
        if i == 0 or sequence[i] != sequence[i - 1]:
            result.append(sequence[i])
    return result
