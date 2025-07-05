import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def visualize_benchmark(input_file="sinkhorn_benchmark_large.csv"):
    df = pd.read_csv(input_file)
    pivot = df.pivot(index="d", columns="n", values="avg_time")

    plt.figure(figsize=(10, 6))
    sns.heatmap(pivot, annot=True, fmt=".3f", cmap="coolwarm", linewidths=0.5)
    plt.title("Temps de l’algorithme Sinkhorn (s)")
    plt.xlabel("n (nombre de points)")
    plt.ylabel("d (dimension)")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    visualize_benchmark()
