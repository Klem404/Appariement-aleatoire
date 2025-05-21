import numpy as np
from scipy.spatial.distance import cdist

def matching_2opt(blue, red, initial_matching=None, p=2, max_iter=1000, return_steps=False):
    n = len(blue)
    if initial_matching is None:
        matching = {i: i for i in range(n)}
        shuffled_values = list(matching.values())
        np.random.shuffle(shuffled_values)
        for idx, val in enumerate(shuffled_values):
            matching[idx] = val
    else:
        matching = initial_matching.copy()

    cost_matrix = cdist(blue, red, metric='minkowski', p=p)

    def total_cost(m):
        return sum(cost_matrix[i, j] for i, j in m.items())

    improved = True
    iter_count = 0

    if return_steps:
        steps = [matching.copy()]
        weights = [total_cost(matching)]
    else:
        steps = None
        weights = None

    while improved and iter_count < max_iter:
        improved = False
        iter_count += 1
        for i1 in range(n):
            for i2 in range(i1 + 1, n):
                j1 = matching[i1]
                j2 = matching[i2]

                old_cost = cost_matrix[i1, j1] + cost_matrix[i2, j2]
                new_cost = cost_matrix[i1, j2] + cost_matrix[i2, j1]

                if new_cost < old_cost:
                    matching[i1] = j2
                    matching[i2] = j1
                    improved = True
                    if return_steps:
                        steps.append(matching.copy())
                        weights.append(total_cost(matching))
                    break
            if improved:
                break

    if return_steps:
        return steps, weights
    else:
        return matching
    
if __name__=="__main__":
    import numpy as np
    import matplotlib.pyplot as plt
    from simul import CubeSimulation
    from matching import Matching
    d=3
    n_points=20
    p=2
    sim = CubeSimulation(d=d,n=n_points)
    sim.generate_points()
    matchings,weights = matching_2opt(sim.blue,sim.red,p=p,return_steps=True)
    sim.represent(matchings,weights=weights)