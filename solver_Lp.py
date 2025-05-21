import numpy as np
from scipy.optimize import linprog
from scipy.spatial.distance import cdist

def solve_optimal_matching(blue_points, red_points, p=2):
    """
    Résout le problème de matching optimal entre points bleus et rouges.
    
    Args:
        blue_points (np.ndarray): tableau (n, d) des points bleus.
        red_points (np.ndarray): tableau (n, d) des points rouges.
        p (float): norme utilisée (par défaut 2 = euclidienne).
        
    Returns:
        dict: dictionnaire {index_bleu: index_rouge} du matching optimal.
    """
    n = len(blue_points)
    assert blue_points.shape == red_points.shape, "Les ensembles de points doivent être de même taille."

    # Étape 1 : créer la matrice de coûts
    cost_matrix = cdist(blue_points, red_points, metric='minkowski', p=p)
    c = cost_matrix.flatten()  # vecteur des coûts pour linprog

    # Étape 2 : construire les contraintes d'égalité
    A_eq = []
    b_eq = []

    # Contraintes : chaque point bleu est apparié à un unique point rouge
    for i in range(n):
        row = np.zeros(n * n)
        row[i * n:(i + 1) * n] = 1
        A_eq.append(row)
        b_eq.append(1)

    # Contraintes : chaque point rouge est apparié à un unique point bleu
    for j in range(n):
        row = np.zeros(n * n)
        row[j::n] = 1
        A_eq.append(row)
        b_eq.append(1)

    A_eq = np.array(A_eq)
    b_eq = np.array(b_eq)

    # Étape 3 : bornes [0,1] pour les variables (on résout la relaxation linéaire)
    bounds = [(0, 1) for _ in range(n * n)]

    # Étape 4 : résolution via linprog
    res = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')

    if not res.success:
        raise ValueError("Problème de résolution du matching : " + res.message)

    x = res.x.reshape((n, n))

    # Étape 5 : récupération d’un matching (on suppose que la solution est entière)
    matching = {}
    for i in range(n):
        j = np.argmax(x[i])
        matching[i] = j

    return matching