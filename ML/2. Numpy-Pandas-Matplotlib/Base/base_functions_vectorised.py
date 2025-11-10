import numpy as np


def get_part_of_array(X: np.ndarray) -> np.ndarray:
    n, m = X.shape
    indices_n = np.arange(0, n, 4)
    indices_m = np.arange(120, 500, 5)
    result = X[indices_n[:, None], indices_m[None, :]]
    return result


def sum_non_neg_diag(X: np.ndarray) -> int:
    n = min(X.shape)
    diagonal = np.diag(X)[:n]
    non_neg_diagonal = diagonal[diagonal >= 0]
    total_sum = np.sum(non_neg_diagonal)
    if total_sum == 0 and len(non_neg_diagonal) == 0:
        return -1
    else:
        return total_sum


def replace_values(X: np.ndarray) -> np.ndarray:
    X_copy = np.array(X, copy=True)
    column = np.mean(X_copy, axis=0)
    upper = 1.5 * column
    lower = 0.25 * column
    mask = (X_copy > upper) | (X_copy < lower)
    X_copy[mask] = -1

    return X_copy