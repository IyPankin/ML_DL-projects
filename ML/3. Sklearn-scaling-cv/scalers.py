import numpy as np
import typing


class MinMaxScaler:
    def fit(self, data: np.ndarray) -> None:
        self.min_ = np.min(data, axis=0)
        self.dif_ = np.max(data, axis=0) - self.min_

    def transform(self, data: np.ndarray) -> np.ndarray:
        data = (data - self.min_) / self.dif_
        return data


class StandardScaler:
    def fit(self, data: np.ndarray) -> None:
        self.mean = np.mean(data, axis=0)
        self.st_d = np.std(data, axis=0)

    def transform(self, data: np.ndarray) -> np.ndarray:
        data = (data - self.mean) / self.st_d
        return data