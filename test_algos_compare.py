import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
from scipy.optimize import linprog
from simul import CubeSimulation
from hungarian_algo import hungarian_algorithm
from sinkhorn_algo import sinkhorn_knopp

def exact_matching_lp(blue, red, p=2):
    n = len(blue)
    C = cdist(blue, red, metric='minkowski', p=p)
    c = C.flatten()
    A_eq = []
    for i in range(n):
        row = np.zeros(n * n)
        row[i * n:(i + 1) * n] = 1
        A_eq.append(row)
    for j in range(n):
        col = np.zeros(n * n)
        col[j::n] = 1
        A_eq.append(col)
    A_eq = np.array(A_eq)
    b_eq = np.ones(2 * n)
    bounds = [(0, 1) for _ in range(n * n)]
    res = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')
    x = res.x.reshape((n, n))
    return {i: int(np.argmax(x[i])) for i in range(n)}

def benchmark_algorithms(trials=10):
    ns = [10, 20,50,100,200,500,700]
    ds = [2,3]
    results = {'Hungarian': [], 'Sinkhorn': [], 'LP': [], 'n': [], 'd': []}

    for d in ds:
        for n in ns:
            times = {'Hungarian': [], 'Sinkhorn': [], 'LP': []}
            for _ in range(trials):
                sim = CubeSimulation(d, n)
                sim.generate_points()
                blue, red = sim.blue, sim.red
                C = cdist(blue, red)

                t0 = time.time()
                _ = hungarian_algorithm(C)
                times['Hungarian'].append(time.time() - t0)

                t0 = time.time()
                _ = sinkhorn_knopp(blue, red)
                times['Sinkhorn'].append(time.time() - t0)

                t0 = time.time()
                _ = exact_matching_lp(blue, red)
                times['LP'].append(time.time() - t0)

            results['n'].append(n)
            results['d'].append(d)
            results['Hungarian'].append(np.mean(times['Hungarian']))
            results['Sinkhorn'].append(np.mean(times['Sinkhorn']))
            results['LP'].append(np.mean(times['LP']))

    return results

def plot_results(results):
    ns = sorted(set(results['n']))
    for d in sorted(set(results['d'])):
        mask = np.array(results['d']) == d
        ns_d = np.array(results['n'])[mask]
        plt.figure(figsize=(10, 6))
        plt.plot(ns_d, np.array(results['Hungarian'])[mask], label='Hungarian')
        plt.plot(ns_d, np.array(results['Sinkhorn'])[mask], label='Sinkhorn')
        plt.plot(ns_d, np.array(results['LP'])[mask], label='Linear Programming')
        plt.title(f'Temps moyen par algo (dimension {d})')
        plt.xlabel('n')
        plt.ylabel('Temps (s)')
        plt.legend()
        plt.grid(True)
        plt.show()

if __name__ == "__main__":
    res = benchmark_algorithms(trials=1)
    plot_results(res)