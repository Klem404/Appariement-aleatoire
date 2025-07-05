import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
from simul import CubeSimulation
from sinkhorn_algo import sinkhorn_knopp
from scipy.optimize import linear_sum_assignment  # Algo hongrois rapide

def compute_matching_cost(blue, red, method='hungarian', p=2):
    C = cdist(blue, red, metric='minkowski', p=p)
    
    if method == 'hungarian':
        row_ind, col_ind = linear_sum_assignment(C)
        return C[row_ind, col_ind].sum()
    
    elif method == 'sinkhorn':
        T = sinkhorn_knopp(blue, red, p=p)
        return np.sum(T * C)

    raise ValueError("Unknown method")

def run_weight_growth_study(d_list, n_list, reps=3, method='hungarian', p=2):
    results = {}

    for d in d_list:
        print(f"\n### Démarrage pour d = {d} ###")
        avg_weights = []
        std_weights = []

        for n in n_list:
            print(f"  → Traitement pour n = {n}...", end=" ", flush=True)
            weights = []
            for rep in range(reps):
                print(f"(essai {rep+1}/{reps})", end=" ", flush=True)
                sim = CubeSimulation(d, n)
                sim.generate_points()
                w = compute_matching_cost(sim.blue, sim.red, method=method, p=p)
                weights.append(w)

            avg = np.mean(weights)
            std = np.std(weights)
            print(f"✓  Moyenne = {avg:.3f}, Écart-type = {std:.3f}")

            avg_weights.append(avg)
            std_weights.append(std)

        results[d] = {
            "n": n_list,
            "mean": avg_weights,
            "std": std_weights
        }

    return results


def plot_weight_growth(results, scale="log", normalize=False):
    plt.figure(figsize=(12, 6))
    
    for d, data in results.items():
        x = np.array(data["n"])
        y = np.array(data["mean"])
        yerr = np.array(data["std"])

        if normalize:
            y = y * (x ** (1/2))  # Juste un exemple
            label = f"d={d} — scaled"
        else:
            label = f"d={d}"

        plt.errorbar(x, y, yerr=yerr, label=label, marker='o', capsize=3)

    plt.xlabel("n (nombre de points)")
    plt.ylabel("Poids moyen du matching")
    plt.xscale(scale)
    if not normalize:
        plt.yscale(scale)
    plt.legend()
    plt.title("Croissance du coût du matching optimal")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def estimate_log_slope(results, p=2):
    dims = []
    alphas = []
    theoricals = []

    for d, data in results.items():
        x = np.log(np.array(data["n"]))
        y = np.log(np.array(data["mean"]))
        coeffs = np.polyfit(x, y, 1)
        alpha = coeffs[0]
        theor = 1 - p / d

        dims.append(d)
        alphas.append(alpha)
        theoricals.append(theor)

        print(f"d = {d} : pente α ≈ {alpha:.4f}, attendu ≈ {theor:.4f}  ⇒ erreur = {abs(alpha - theor):.4f}")

    # Affichage matplotlib
    plt.figure(figsize=(8, 5))
    plt.plot(dims, alphas, 'o-', label='Pente estimée', color='tab:blue')
    plt.plot(dims, theoricals, '--', label='Pente attendue $1 - \\frac{p}{d}$', color='tab:orange')

    for i, d in enumerate(dims):
        plt.text(d, alphas[i] + 0.01, f"{alphas[i]:.2f}", ha='center', fontsize=9)

    plt.xlabel("Dimension $d$")
    plt.ylabel("Pente estimée $\\alpha$")
    plt.title("Comparaison pente alpha estimée vs attendue")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    d_vals = [ 3,5,7,10,15,20,30,40,50]
    n_vals = [100,200,500,1000,2000,5000,10000,20000]
    results = run_weight_growth_study(d_vals, n_vals, reps=2, method='hungarian', p=2)
    plot_weight_growth(results, scale="log", normalize=False)
    estimate_log_slope(results)
    estimate_log_slope(results)