import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler


def train_svm_and_predict(train_features, train_target, test_features):
    model = SVC(kernel='rbf', C=460, gamma=0.01)
    model.fit(train_features[:, 2:], train_target)
    pred = model.predict(test_features[:, 2:])
    return pred
