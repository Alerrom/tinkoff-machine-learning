import numpy as np
from typing import Optional, Union, Tuple


def euclidean_distance(x: np.array, y: np.array) -> float:
    return sum((x - y) ** 2) ** 0.5
    pass


def euclidean_similarity(x: np.array, y: np.array) -> float:
    return 1 / (1 + euclidean_distance(x, y))
    pass


def pearson_similarity(x: np.array, y: np.array) -> float:
    return sum((x - x.mean()) * (y - y.mean())) / ((sum((x - x.mean()) ** 2) * sum((y - y.mean()) ** 2)) ** 0.5)
    pass


def apk(actual: np.array, predicted: np.array, k: int = 10) -> float:
    if k < len(predicted):
        predicted = predicted[:k]

    score = 0
    num_hits = 0

    for i, p in enumerate(predicted):
        if p in actual and p not in predicted[:i]:
            num_hits += 1
            score += num_hits / (i + 1)

    return score / min(len(actual), k)
    pass


def mapk(actual: np.array, predicted: np.array, k: int = 10) -> float:
    return np.mean([apk(act, pred, k) for act, pred in zip(actual, predicted)])
    pass
