import numpy as np
import matplotlib.pyplot as plt

from simul import CubeSimulation
from matching import Matching
from heuristic1 import heuristic_greedy
from heuristic2 import heuristic_nearest_neighbor
from solver_Lp import solve_optimal_matching  
from heuristic3 import matching_2opt

def evaluate_heuristics(n_runs=50, n_points=30, d=2, p=2):
    heuristics = {
        "Greedy": heuristic_greedy,
        "NearestNeighbor": heuristic_nearest_neighbor,
        "2Improvement" : matching_2opt,
        "LinProg (optimal)":solve_optimal_matching
    }

    results = {name: [] for name in heuristics}

    for _ in range(n_runs):
        sim = CubeSimulation(d, n_points)
        sim.generate_points()

        for name, algo in heuristics.items():
            match_dict = algo(sim.blue, sim.red, p=p)
            m = Matching(sim.blue, sim.red, match_dict, p=p)
            results[name].append(m.total_cost())

    return results

def plot_results(results,n_runs=50, n_points=30, d=2, p=2):
    labels = list(results.keys())
    data = [results[label] for label in labels]

    plt.figure(figsize=(10, 6))
    plt.boxplot(data, labels=labels)
    plt.ylabel("Coût total du matching")
    plt.title(f"Comparaison des heuristiques   {n_runs} essais pour {n_points} points\n dim = {d} {p=}")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    n_runs=200
    n_points=30
    d=5
    p=2
    results = evaluate_heuristics(n_runs=n_runs, n_points=n_points, d=d, p=p)
    plot_results(results,n_runs=n_runs, n_points=n_points, d=d, p=p)
