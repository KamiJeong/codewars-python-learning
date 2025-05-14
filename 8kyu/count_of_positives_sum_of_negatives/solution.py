def count_positives_sum_negatives(arr : list[int]) -> list[int]:
    if  not arr:
        return []
    else:
        sum_positive = 0
        sum_negative = 0
        for num in arr:
            if num > 0:
                sum_positive += 1
            elif num < 0:
                sum_negative += num
        return [sum_positive, sum_negative]
