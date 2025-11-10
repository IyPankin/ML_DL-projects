import numpy as np


def evaluate_measures(sample):

    unq, cs = np.unique(sample, return_counts=True)
    probs = cs / np.sum(cs)
    gini = 1 - np.dot(probs, probs)
    entropy = -np.dot(probs, np.log(np.clip(probs, 1e-10, 1)))
    error = 1 - np.max(probs)
    measures = {'gini': float(gini), 'entropy': float(entropy), 'error': float(error)}
    return measures
