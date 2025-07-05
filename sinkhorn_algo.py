import numpy as np
from scipy.spatial.distance import cdist

def sinkhorn_knopp(blue, red, p=2, reg=0.01, num_iters=100):
    n = len(blue)
    C = cdist(blue, red, metric='minkowski', p=p)
    K = np.exp(-C / reg)

    u = np.ones(n)
    v = np.ones(n)
    for _ in range(num_iters):
        u = 1.0 / (K @ v)
        v = 1.0 / (K.T @ u)

    P = np.diag(u) @ K @ np.diag(v)
    matching = {}
    for i in range(n):
        j = np.argmax(P[i])
        matching[i] = j

    return matching

