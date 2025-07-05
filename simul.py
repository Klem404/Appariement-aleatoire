from random import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider,Button
from mpl_toolkits.mplot3d import Axes3D
class CubeSimulation:
    def __init__(self,d:int,n:int):
        self.d =d 
        self.n=n
        self.blue = [] 
        self.red = [] 
        
    def generate_point(self):
        return np.array([random() for _ in range(self.d)])
        
    def generate_points(self):
        self.blue = np.array([self.generate_point() for _ in range(self.n)])
        self.red = np.array([self.generate_point() for _ in range(self.n)])
        
    def __str__(self):
        s=f"Dimension : {self.d}\n"
        s+=f"{self.n=}\n"
        s+="Points bleus : "+str(self.blue)+"\n"
        s+="Points rouges"+str(self.red)
        return s
        
    def represent(self, matching=None, weights=None):
        if not isinstance(matching, list):
            matching = [matching]

        step = {'index': 0}
        num_steps = len(matching)

        fig = plt.figure(figsize=(8, 8) if self.d == 3 else (6, 6))
        if self.d == 3:
            ax = fig.add_subplot(111, projection='3d')
        else:
            ax = fig.add_subplot(111)

        # Slider
        slider_ax = fig.add_axes([0.2, 0.02, 0.6, 0.03])
        slider = Slider(slider_ax, 'Étape', 0, num_steps - 1, valinit=0, valstep=1)

        # Si les poids ne sont pas fournis, on les calcule par défaut avec p=2
        if weights is None:
            from scipy.spatial.distance import cdist
            cost_matrix = cdist(self.blue, self.red, metric='minkowski', p=2)
            weights = []
            for m in matching:
                if m is None:
                    weights.append(0.0)
                else:
                    weights.append(sum(cost_matrix[i, j] for i, j in m.items()))

        def draw(index):
            ax.clear()
            if self.d == 2:
                ax.scatter(self.blue[:, 0], self.blue[:, 1], c='blue', label='Points bleus', alpha=0.7)
                ax.scatter(self.red[:, 0], self.red[:, 1], c='red', label='Points rouges', alpha=0.7)
                ax.set_xlim(0, 1)
                ax.set_ylim(0, 1)
                ax.grid(True)

                m = matching[index]
                if m is not None:
                    for bleu_idx, rouge_idx in m.items():
                        ax.plot([self.blue[bleu_idx, 0], self.red[rouge_idx, 0]],
                                [self.blue[bleu_idx, 1], self.red[rouge_idx, 1]],
                                'k-', linewidth=2, alpha=0.9)

            elif self.d == 3:
                ax.scatter(self.blue[:, 0], self.blue[:, 1], self.blue[:, 2], c='blue', alpha=0.7)
                ax.scatter(self.red[:, 0], self.red[:, 1], self.red[:, 2], c='red', alpha=0.7)
                ax.set_xlim(0, 1)
                ax.set_ylim(0, 1)
                ax.set_zlim(0, 1)

                m = matching[index]
                if m is not None:
                    for bleu_idx, rouge_idx in m.items():
                        ax.plot([self.blue[bleu_idx, 0], self.red[rouge_idx, 0]],
                                [self.blue[bleu_idx, 1], self.red[rouge_idx, 1]],
                                [self.blue[bleu_idx, 2], self.red[rouge_idx, 2]],
                                'k-', linewidth=2, alpha=0.9)

            ax.set_title(f"Poids total : {weights[index]:.4f}")
            fig.canvas.draw_idle()

        def on_slider_change(val):
            step['index'] = int(val)
            draw(step['index'])

        slider.on_changed(on_slider_change)
        draw(0)
        plt.show()
        
    @classmethod
    def see_solution(self, matching, weight):
        fig = plt.figure(figsize=(8, 8) if self.d == 3 else (6, 6))
        if self.d == 3:
            ax = fig.add_subplot(111, projection='3d')
        else:
            ax = fig.add_subplot(111)

        # Créer l'espace pour le bouton
        button_ax = fig.add_axes([0.7, 0.02, 0.2, 0.05])
        button = Button(button_ax, 'Afficher matching')
        show_edges = {'visible': False}

        def draw():
            ax.clear()

            # Scatter points
            if self.d == 2:
                ax.scatter(self.blue[:, 0], self.blue[:, 1], c='blue', label='Points bleus', alpha=0.7)
                ax.scatter(self.red[:, 0], self.red[:, 1], c='red', label='Points rouges', alpha=0.7)
                ax.set_xlim(0, 1)
                ax.set_ylim(0, 1)
                ax.grid(True)
            elif self.d == 3:
                ax.scatter(self.blue[:, 0], self.blue[:, 1], self.blue[:, 2], c='blue', alpha=0.7)
                ax.scatter(self.red[:, 0], self.red[:, 1], self.red[:, 2], c='red', alpha=0.7)
                ax.set_xlim(0, 1)
                ax.set_ylim(0, 1)
                ax.set_zlim(0, 1)

            # Draw matching lines if toggled
            if show_edges['visible']:
                if self.d == 2:
                    for b, r in matching.items():
                        ax.plot([self.blue[b, 0], self.red[r, 0]],
                                [self.blue[b, 1], self.red[r, 1]],
                                'k-', linewidth=2, alpha=0.9)
                elif self.d == 3:
                    for b, r in matching.items():
                        ax.plot([self.blue[b, 0], self.red[r, 0]],
                                [self.blue[b, 1], self.red[r, 1]],
                                [self.blue[b, 2], self.red[r, 2]],
                                'k-', linewidth=2, alpha=0.9)
                ax.set_title(f"Matching optimal — poids total : {weight:.4f}")
            else:
                ax.set_title("Points générés")

            fig.canvas.draw_idle()

        def toggle(event):
            show_edges['visible'] = not show_edges['visible']
            button.label.set_text("Cacher matching" if show_edges['visible'] else "Afficher matching")
            draw()

        button.on_clicked(toggle)
        draw()
        plt.show()

            
if __name__ == "__main__":
    Cube2 = CubeSimulation(2,30)
    Cube2.generate_points()
    Cube2.represent(matching = [{i:i for i in range(30)}])
    # Cube3 = CubeSimulation(3,50)
    # Cube3.generate_points()
    # Cube3.represent(matching = {i:i for i in range(50)})