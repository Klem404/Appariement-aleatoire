import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
from hungarian_algo import hungarian_algorithm
from simul import CubeSimulation

def test_matching_times(n_values, d_values, trials=3):
    results = {}
    for d in d_values:
        for n in n_values:
            total_time = 0.0
            for _ in range(trials):
                sim = CubeSimulation(d, n)
                sim.generate_points()
                C = cdist(sim.blue, sim.red, metric='euclidean')
                start = time.time()
                _ = hungarian_algorithm(C)
                total_time += time.time() - start
            avg_time = total_time / trials
            results[(n, d)] = avg_time
            print(f"d={d}, n={n}, time={avg_time:.4f}s")
    return results

def plot_results(results):
    import matplotlib.cm as cm
    import matplotlib.colors as mcolors

    n_values = sorted(set(k[0] for k in results))
    d_values = sorted(set(k[1] for k in results))

    fig, ax = plt.subplots(figsize=(10, 6))
    cmap = cm.get_cmap("viridis", len(d_values))
    norm = mcolors.Normalize(vmin=min(d_values), vmax=max(d_values))

    for idx, d in enumerate(d_values):
        times = [results[(n, d)] for n in n_values]
        ax.plot(n_values, times, label=f"d={d}", marker='o', color=cmap(norm(d)))

    ax.set_title("Temps de r\u00e9solution (algo Hongrois)")
    ax.set_xlabel("n (nombre de points)")
    ax.set_ylabel("Temps moyen (secondes)")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.grid(True, which='both', linestyle='--', alpha=0.6)
    ax.legend(title="Dimensions", loc='upper left', fontsize='small')
    plt.tight_layout()
    plt.show()

def plot_subplots(results):
    n_values = sorted(set(k[0] for k in results))
    d_values = sorted(set(k[1] for k in results))
    num_cols = 3
    num_rows = int(np.ceil(len(d_values) / num_cols))

    fig, axs = plt.subplots(num_rows, num_cols, figsize=(15, 4 * num_rows))
    axs = axs.flatten()

    for i, d in enumerate(d_values):
        times = [results[(n, d)] for n in n_values]
        ax = axs[i]
        ax.plot(n_values, times, marker='o')
        ax.set_title(f"Temps pour d = {d}")
        ax.set_xlabel("n")
        ax.set_ylabel("temps (s)")
        ax.set_xscale("log")
        ax.set_yscale("log")
        ax.grid(True, which='both', linestyle='--', alpha=0.6)

    for j in range(i+1, len(axs)):
        fig.delaxes(axs[j])

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    n_values = [10, 20, 40, 80, 160, 320]
    d_values = [1, 2, 4, 8, 16]

    results = test_matching_times(n_values, d_values, trials=3)
    plot_results(results)
    plot_subplots(results)
