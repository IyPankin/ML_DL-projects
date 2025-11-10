from typing import List
from copy import deepcopy


def get_part_of_array(X: List[List[float]]) -> List[List[float]]:
    n, m = len(X), len(X[0])
    result = []
    indices_n = range(0, n, 4)
    indices_m = range(120, 500, 5)
    for i in indices_n:
        row = []
        for j in indices_m:
            row.append(X[i][j])
        result.append(row)

    return result


def sum_non_neg_diag(X: List[List[int]]) -> int:
    total_sum = 0
    n, m = len(X), len(X[0])
    for i in range(min(n, m)):
        if X[i][i] >= 0:
            total_sum += X[i][i]
    if total_sum == 0 and any(X[i][i] < 0 for i in range(min(n, m))):
        return -1
    else:
        return total_sum


def replace_values(X: List[List[float]]) -> List[List[float]]:
    X_copy = deepcopy(X)
    column = [sum(col) / len(col) for col in zip(*X_copy)]
    upper = [1.5 * col for col in column]
    lower = [0.25 * col for col in column]
    for i in range(len(X_copy)):
        for j in range(len(X_copy[0])):
            if X_copy[i][j] > upper[j] or X_copy[i][j] < lower[j]:
                X_copy[i][j] = -1

    return X_copy