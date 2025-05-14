def tribonacci(signature: list[int], n: int) -> list[int]:
    if n == 0:
        return []
    if n <= len(signature):
        return signature[:n]
    result = signature[:]
    for i in range(n - len(signature)):
        result.append(sum(result[-3:]))
    return result
