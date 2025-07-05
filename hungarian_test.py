import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
import time
from simul import CubeSimulation
from hungarian_algo import hungarian_algorithm

def test_scaling(p=2):
    ns = [50, 75, 100, 150, 200, 250, 300, 400, 500, 600, 700]
    ds = [2, 3]

    results = {d: [] for d in ds}

    print("Running scaling test...\n")
    for d in ds:
        print(f"--- Dimension d = {d} ---")
        for n in ns:
            sim = CubeSimulation(d, n)
            sim.generate_points()
            blue, red = sim.blue, sim.red

            C = cdist(blue, red, metric='minkowski', p=p)
            start = time.time()
            _ = hungarian_algorithm(C)
            elapsed = time.time() - start
            print(f"n = {n}: {elapsed:.4f}s")
            results[d].append(elapsed)

    # --- Affichage ---
    plt.figure(figsize=(10, 7))

    # Résultats empiriques
    for d in ds:
        plt.plot(ns, results[d], marker='o', label=f'Hongrois (d={d})')

    # Références théoriques (normalisées pour lisibilité)
    ns_arr = np.array(ns)
    def normalize(ref):
        return ref / ref[-1] * max(results[ds[0]])  # normalise à l’échelle des données

    plt.plot(ns, normalize(ns_arr**2), '--', label=r'$O(n^2)$', color='gray')
    plt.plot(ns, normalize(ns_arr**3), '--', label=r'$O(n^3)$', color='black')

    # Style
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel("n (log)")
    plt.ylabel("Temps (s, log)")
    plt.title("Temps d'exécution — Algorithme hongrois")
    plt.grid(True, which='both', linestyle='--', alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    test_scaling()
