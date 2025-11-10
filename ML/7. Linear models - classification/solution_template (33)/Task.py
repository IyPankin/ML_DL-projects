import numpy as np


class Preprocessor:

    def __init__(self):
        pass

    def fit(self, X, Y=None):
        pass

    def transform(self, X):
        pass

    def fit_transform(self, X, Y=None):
        pass


class MyOneHotEncoder(Preprocessor):

    def __init__(self, dtype=np.float64):
        super(Preprocessor).__init__()
        self.dtype = dtype

    def fit(self, X, Y=None):
        ans = []
        x = X.to_numpy()
        for j in range(x.shape[1]):
            tmp = []
            for i in range(x.shape[0]):
                if x[i][j] not in tmp:
                    tmp.append(x[i][j])
            ans.append(sorted(tmp))
        self.unique = ans

    def transform(self, X):
        ans = None
        x = X.to_numpy()
        for j in range(x.shape[1]):
            tmp = np.zeros((x.shape[0], len(self.unique[j])))
            for i in range(x.shape[0]):
                for index, elem in enumerate(self.unique[j]):
                    if elem == x[i][j]:
                        tmp[i][index] = 1
                        break
            if ans is None:
                ans = tmp
            else:
                ans = np.concatenate((ans, tmp), axis=1)
        return ans

    def fit_transform(self, X, Y=None):
        self.fit(X)
        return self.transform(X)

    def get_params(self, deep=True):
        return {"dtype": self.dtype}


class SimpleCounterEncoder:

    def __init__(self, dtype=np.float64):
        self.dtype = dtype

    def fit(self, X, Y):
        x = X.to_numpy()
        y = Y.to_numpy()
        ans = []
        for j in range(x.shape[1]):
            tmp = {}
            for i in range(x.shape[0]):
                if x[i][j] not in tmp:
                    counters = 0
                    successes = 0
                    for i1 in range(x.shape[0]):
                        if x[i1][j] == x[i][j]:
                            counters += 1
                            successes += y[i1]
                    successes = successes / counters
                    counters = counters / x.shape[0]
                    tmp[x[i][j]] = np.array([successes, counters, 0])
            ans.append(tmp)
        self.dict = ans

    def transform(self, X, a=1e-5, b=1e-5):
        ans = None
        x = X.to_numpy()
        for j in range(x.shape[1]):
            tmp = np.zeros((x.shape[0], 3))
            for i in range(x.shape[0]):
                tmp[i] = self.dict[j][x[i][j]]
                tmp[i][2] = (tmp[i][0] + a) / (tmp[i][1] + b)
            if ans is None:
                ans = tmp
            else:
                ans = np.concatenate((ans, tmp), axis=1)
        return ans

    def fit_transform(self, X, Y, a=1e-5, b=1e-5):
        self.fit(X, Y)
        return self.transform(X, a, b)

    def get_params(self, deep=True):
        return {"dtype": self.dtype}


def group_k_fold(size, n_splits=3, seed=1):
    idx = np.arange(size)
    np.random.seed(seed)
    idx = np.random.permutation(idx)
    n_ = size // n_splits
    for i in range(n_splits - 1):
        yield idx[i * n_: (i + 1) * n_], np.hstack((idx[:i * n_], idx[(i + 1) * n_:]))
    yield idx[(n_splits - 1) * n_:], idx[:(n_splits - 1) * n_]


class FoldCounters:

    def __init__(self, n_folds=3, dtype=np.float64):
        self.dtype = dtype
        self.n_folds = n_folds

    def fit(self, X, Y, seed=1):
        self.groups = group_k_fold(X.shape[0], self.n_folds, seed)
        ans = []
        for val, train in self.groups:
            sce = SimpleCounterEncoder()
            sce.fit(X.iloc[train], Y.iloc[train])
            ans.append((val, sce))
        self.ans = ans

    def transform(self, X, a=1e-5, b=1e-5):
        tmp = None
        for val, class1 in self.ans:
            print(type(val))
            con = np.concatenate((class1.transform(X.iloc[val], a, b), np.reshape(np.array(val), (len(val), 1))), axis=1)
            if tmp is None:
                tmp = con
            else:
                tmp = np.concatenate((tmp, con), axis=0)
        tmp = tmp[tmp[:, -1].argsort()]
        return np.delete(tmp, -1, 1)

    def fit_transform(self, X, Y, a=1e-5, b=1e-5):
        self.fit(X, Y)
        return self.transform(X, a, b)


def weights(x, y):
    set_tmp = set(x)
    w = np.array([0.0]*len(set_tmp))
    for i, elem in enumerate(set_tmp):
        w[i] = sum(y[x == elem]) / list(x).count(elem)
    return w
