import numpy as np
import matplotlib.pyplot as plt
from solver_Lp import solve_optimal_matching
from simul import CubeSimulation
from matching import Matching

def run_tests(n_tests=1000, n_points=30, d=2, p_values=[1, 2, 3, np.inf]):
    results = {p: [] for p in p_values}

    for p in p_values:
        print(f"Lancement des tests pour p = {p}...")
        for _ in range(n_tests):
            cube = CubeSimulation(d, n_points)
            cube.generate_points()
            matching_dict = solve_optimal_matching(cube.blue, cube.red, p=p)
            matching = Matching(cube.blue, cube.red, matching_dict, p=p)
            results[p].append(matching.total_cost())

    return results

def plot_histograms(results,n_tests=1000, n_points=30, d=2, p_values=[1, 2, 3, np.inf]):
    p_values = list(results.keys())
    fig, axs = plt.subplots(1, len(p_values), figsize=(18, 4))

    for i, p in enumerate(p_values):
        axs[i].hist(results[p], bins=20, color='skyblue', edgecolor='black')
        axs[i].set_title(f'Norme p = {p}')
        axs[i].set_xlabel('Coût total')
        axs[i].set_ylabel('Fréquence')
        axs[i].grid(True)

    plt.suptitle(f'Distribution du coût total du matching optimal ({n_tests} essais)\n dim={d}, {n_points=}')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    n_tests,n_points,d=1000,30,4
    results = run_tests(n_tests=n_tests,n_points=n_points,d=d)
    plot_histograms(results,n_tests=n_tests,n_points=n_points,d=d)
