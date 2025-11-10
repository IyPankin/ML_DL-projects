from collections import Counter
from typing import List


def are_multisets_equal(x: List[int], y: List[int]) -> bool:
    x_sorted = sorted(x)
    y_sorted = sorted(y)
    return x_sorted == y_sorted


def max_prod_mod_3(x: List[int]) -> int:
    result = -1
    for i in range(len(x) - 1):
        if (x[i] % 3 == 0 or x[i + 1] % 3 == 0):
            product = x[i] * x[i + 1]
            result = max(result, product)
    if result == -1:
        return -1
    return result


def convert_image(image: List[List[List[float]]], weights: List[float]) -> List[List[float]]:
    height, width, num_channels = len(image), len(image[0]), len(image[0][0])
    result = [[0 for _ in range(width)] for _ in range(height)]
    for i in range(height):
        for j in range(width):
            for k in range(num_channels):
                result[i][j] += image[i][j][k] * weights[k]

    return result


def rle_scalar(x: List[List[int]], y:  List[List[int]]) -> int:
    def decode_rle(rle_vector):
        decoded_vector = []
        for element, count in rle_vector:
            decoded_vector.extend([element] * count)
        return decoded_vector

    x_rle = decode_rle(x)
    y_rle = decode_rle(y)
    if len(x_rle) != len(y_rle):
        return -1
    return sum(a * b for a, b in zip(x_rle, y_rle))


def cosine_distance(X: List[List[float]], Y: List[List[float]]) -> List[List[float]]:
    n, m, d = len(X), len(Y), len(X[0])
    M = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            dot_product = sum(x * y for x, y in zip(X[i], Y[j]))
            norm_X = (sum(x ** 2 for x in X[i])) ** 0.5
            norm_Y = (sum(y ** 2 for y in Y[j])) ** 0.5
            if norm_X == 0 or norm_Y == 0:
                M[i][j] = 1
            else:
                M[i][j] = dot_product / (norm_X * norm_Y)
    return M