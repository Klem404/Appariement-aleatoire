from random import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
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
        
    def represent(self, matching=None):
        if not isinstance(matching, list):
            matching = [matching]

        step = {'index': 0}
        num_steps = len(matching)

        fig = plt.figure(figsize=(8, 8) if self.d == 3 else (6, 6))
        if self.d == 3:
            from mpl_toolkits.mplot3d import Axes3D
            ax = fig.add_subplot(111, projection='3d')
        else:
            ax = fig.add_subplot(111)

        # Crée une zone pour le slider
        slider_ax = fig.add_axes([0.2, 0.02, 0.6, 0.03])
        slider = Slider(slider_ax, 'Étape', 0, num_steps - 1, valinit=0, valstep=1)

        def draw(index):
            ax.clear()
            if self.d == 2:
                ax.scatter(self.blue[:,0], self.blue[:,1], c='blue', label='Points bleus', alpha=0.7)
                ax.scatter(self.red[:,0], self.red[:,1], c='red', label='Points rouges', alpha=0.7)
                ax.set_title(f"Étape {index + 1}/{num_steps}")
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
                ax.scatter(self.blue[:,0], self.blue[:,1], self.blue[:,2], c='blue', alpha=0.7)
                ax.scatter(self.red[:,0], self.red[:,1], self.red[:,2], c='red', alpha=0.7)
                ax.set_xlim(0, 1)
                ax.set_ylim(0, 1)
                ax.set_zlim(0, 1)
                ax.set_title(f"Étape {index + 1}/{num_steps}")

                m = matching[index]
                if m is not None:
                    for bleu_idx, rouge_idx in m.items():
                        ax.plot([self.blue[bleu_idx,0], self.red[rouge_idx,0]],
                                [self.blue[bleu_idx,1], self.red[rouge_idx,1]],
                                [self.blue[bleu_idx,2], self.red[rouge_idx,2]],
                                'k-', linewidth=2, alpha=0.9)

            fig.canvas.draw_idle()

        def on_slider_change(val):
            step['index'] = int(val)
            draw(step['index'])

        slider.on_changed(on_slider_change)
        draw(0)
        plt.show()

            
if __name__ == "__main__":
    Cube2 = CubeSimulation(2,30)
    Cube2.generate_points()
    Cube2.represent(matching = [{i:i for i in range(30)},{i:29-i for i in range(30)},{i: (i + 1) % 30 for i in range(30)}])
    # Cube3 = CubeSimulation(3,50)
    # Cube3.generate_points()
    # # Cube3.represent(matching = {i:i for i in range(50)})