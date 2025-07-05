import numpy as np

class Matching:
    def __init__(self, blue_points, red_points, matching_dict, p=2):
        """
        Initialise un matching rouge-bleu.
        
        Args:
            blue_points (np.ndarray): Tableau (n, d) des points bleus.
            red_points (np.ndarray): Tableau (n, d) des points rouges.
            matching_dict (dict): Dictionnaire {i_b: i_r} représentant les appariements.
            p (float): Norme utilisée (par défaut euclidienne, p=2).
        """
        self.blue = blue_points
        self.red = red_points
        self.matching = matching_dict
        self.p = p

        self._check_integrity()

    def _check_integrity(self):
        """Vérifie que chaque point bleu est apparié une seule fois et que tous les indices sont valides."""
        n = len(self.blue)
        if len(self.matching) != n:
            raise ValueError("Le matching ne couvre pas tous les points bleus.")
        
        if len(set(self.matching.values())) != n:
            raise ValueError("Plusieurs points bleus sont appariés au même point rouge.")

        if any(i not in range(n) for i in self.matching.keys()):
            raise IndexError("Index de point bleu invalide dans le matching.")
        
        if any(j not in range(n) for j in self.matching.values()):
            raise IndexError("Index de point rouge invalide dans le matching.")

    def total_cost(self):
        """Calcule la somme des distances entre les points matchés."""
        cost = 0.0
        for i_b, i_r in self.matching.items():
            dist = np.linalg.norm(self.blue[i_b] - self.red[i_r], ord=self.p)
            cost += dist
        return cost

    def print_summary(self):
        """Affiche un résumé textuel du matching."""
        print(f"Matching de {len(self.matching)} paires en dimension {self.blue.shape[1]}")
        print(f"Norme utilisée : L^{self.p}")
        print(f"Coût total du matching : {self.total_cost():.4f}")

    def get_edges(self):
        """
        Retourne les couples de points appariés (utile pour affichage ou analyse).
        
        Returns:
            List of tuples: [(blue_point, red_point), ...]
        """
        return [(self.blue[i_b], self.red[i_r]) for i_b, i_r in self.matching.items()]
