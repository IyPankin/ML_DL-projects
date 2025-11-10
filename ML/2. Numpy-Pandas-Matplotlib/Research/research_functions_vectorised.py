import numpy as np


def are_multisets_equal(x: np.ndarray, y: np.ndarray) -> bool:
    x_sorted = np.sort(x)
    y_sorted = np.sort(y)
    return np.array_equal(x_sorted, y_sorted)


def max_prod_mod_3(x: np.ndarray) -> int:
    x = np.array(x)
    mask = (x % 3 == 0)
    pairs = np.stack((x[:-1], x[1:]), axis=1)
    filtr = pairs[mask[:-1] | mask[1:]]
    result = filtr[:, 0] * filtr[:, 1]
    if len(result) == 0:
        return -1
    else:
        return np.max(result)


def convert_image(image: np.ndarray, weights: np.ndarray) -> np.ndarray:
    weights = np.array(weights)
    weighted_sum = np.sum(image * weights, axis=-1)
    return weighted_sum


def rle_scalar(x: np.ndarray, y: np.ndarray) -> int:
    def decode_rle(rle_vector):
        return np.repeat(rle_vector[:, 0], rle_vector[:, 1])

    x_rle = decode_rle(x)
    y_rle = decode_rle(y)
    if len(x_rle) != len(y_rle):
        return -1
    return np.dot(x_rle, y_rle)


def cosine_distance(X: np.ndarray, Y: np.ndarray) -> np.ndarray:
    dot_products = np.dot(X, Y.T)
    X_norm = np.linalg.norm(X, axis=1, keepdims=True)
    Y_norm = np.linalg.norm(Y, axis=1, keepdims=True)
    result = dot_products / (np.dot(X_norm, Y_norm.T))
    result[np.isnan(result)] = 1
    return result