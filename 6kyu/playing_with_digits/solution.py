def dig_pow(n: int, p: int) -> float | int:
    if p == 0 or n == 0:
        return -1
    digits = [int(d) ** (p + i) for i, d in enumerate(str(n))]
    total = sum(digits)

    return total / n if (total % n == 0) else -1
