import numpy as np
from scipy.spatial.distance import cdist

def heuristic_greedy(blue, red, p=2):
    n = len(blue)
    remaining_blue = list(range(n))
    remaining_red = list(range(n))
    matching = {}

    cost_matrix = cdist(blue, red, metric='minkowski', p=p)
    pairs = [(i, j, cost_matrix[i][j]) for i in range(n) for j in range(n)]
    pairs.sort(key=lambda x: x[2])

    for i, j, _ in pairs:
        if i in remaining_blue and j in remaining_red:
            matching[i] = j
            remaining_blue.remove(i)
            remaining_red.remove(j)

    return matching
