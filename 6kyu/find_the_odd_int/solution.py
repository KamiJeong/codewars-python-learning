def find_it(seq: list[int]) -> int | None:
    # Loot the odd integers in the sequence
    # and return the one that appears an odd number of times
    # Use a dictionary to count occurrences
    counts = {}
    for num in seq:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    # Find the number with an odd count
    for num, count in counts.items():
        if count % 2 != 0:
            return num
    return None  # In case there is no odd integer

