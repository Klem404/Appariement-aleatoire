from simul import CubeSimulation
from matching import Matching
from solver_Lp import solve_optimal_matching

def main():
    # Paramètres
    dimension = 2
    nb_points = 20
    p_norm = 2

    # Générer points aléatoires
    sim = CubeSimulation(dimension, nb_points)
    sim.generate_points()

    # Résolution PL
    matching_dict = solve_optimal_matching(sim.blue, sim.red, p=p_norm)

    # Créer l'objet Matching
    matching_obj = Matching(sim.blue, sim.red, matching_dict, p=p_norm)

    # Vérification de l'intégrité
    assert matching_obj.total_cost() > 0, "Matching vide ou incorrect."
    print("Matching valide ✔")
    matching_obj.print_summary()

    # Affichage
    sim.see_solution(matching=matching_dict,weight=matching_obj.total_cost())

if __name__ == "__main__":
    main()
