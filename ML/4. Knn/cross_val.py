import numpy as np
import typing
from collections import defaultdict


def kfold_split(num_objects: int,
                num_folds: int) -> list[tuple[np.ndarray, np.ndarray]]:
    indices = np.arange(num_objects)
    fold_size = num_objects // num_folds
    folds = []
    start = 0
    for i in range(num_folds - 1):
        end = start + fold_size
        folds.append(indices[start:end])
        start = end
    folds.append(indices[start:])
    result = []
    for i in range(num_folds):
        train_ind = np.concatenate([folds[j] for j in range(num_folds) if j != i])
        test_ind = folds[i]
        result.append((train_ind, test_ind))
    return result


def knn_cv_score(X, y, parameters, score_function, folds, knn_class):
    result = {}
    for n_neighbors in parameters['n_neighbors']:
        for metrics in parameters['metrics']:
            for weights in parameters['weights']:
                for normalizers in parameters['normalizers']:
                    score = 0
                    for train_idx, val_idx in folds:
                        X_train = X[train_idx]
                        X_val = X[val_idx]
                        y_train = y[train_idx]
                        y_val = y[val_idx]
                        if normalizers[0]:
                            normalizers[0].fit(X_train)
                            X_train = normalizers[0].transform(X_train)
                            X_val = normalizers[0].transform(X_val)
                        model = knn_class(n_neighbors=n_neighbors, metric=metrics, weights=weights)
                        model.fit(X=X_train, y=y_train)
                        tmp = model.predict(X_val)
                        score += score_function(y_val, tmp)
                    score /= len(folds)
                    result[(normalizers[1], n_neighbors, metrics, weights)] = score
    return result