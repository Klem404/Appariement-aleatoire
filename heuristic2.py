import numpy as np
from scipy.spatial.distance import cdist

def heuristic_nearest_neighbor(blue, red, p=2):
    n = len(blue)
    remaining_red = set(range(n))
    matching = {}

    cost_matrix = cdist(blue, red, metric='minkowski', p=p)

    for i in range(n):
        # Trouve le point rouge le plus proche parmi ceux qui restent
        distances = [(j, cost_matrix[i][j]) for j in remaining_red]
        j_min = min(distances, key=lambda x: x[1])[0]
        matching[i] = j_min
        remaining_red.remove(j_min)

    return matching
