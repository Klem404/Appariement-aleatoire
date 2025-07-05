import numpy as np
import time
import csv
from simul import CubeSimulation
from sinkhorn_algo import sinkhorn_knopp

def benchmark_sinkhorn(ns, ds, repetitions=1, output_file="sinkhorn_benchmark_large.csv"):
    with open(output_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["n", "d", "avg_time", "std_time"])

        for d in ds:
            for n in ns:
                times = []
                for _ in range(repetitions):
                    sim = CubeSimulation(d, n)
                    sim.generate_points()
                    blue, red = sim.blue, sim.red

                    start = time.time()
                    _ = sinkhorn_knopp(blue, red)
                    times.append(time.time() - start)

                avg_time = np.mean(times)
                std_time = np.std(times)
                writer.writerow([n, d, avg_time, std_time])
                print(f"n={n}, d={d} → time: {avg_time:.5f}s")

if __name__ == "__main__":
    ns = list(range(100, 2100, 100))  # 100 to 2000 by 100
    ds = [2, 5, 10, 20, 50, 100]
    benchmark_sinkhorn(ns, ds)
