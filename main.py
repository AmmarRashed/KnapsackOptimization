import csv
from argparse import ArgumentParser
import matplotlib.pyplot as plt
from simulated_annealing import SimulatedAnnealing


def parse_data(path):
    with open(path, mode='r') as file:
        # reading the CSV file
        v, w = [], []
        for i, line in enumerate(csv.reader(file)):
            if i == 0:  # skip header
                continue
            v.append(int(line[0]))
            w.append(int(line[1]))
    return v, w


def plot_results(values, weights, max_weight):
    ax, fig = plt.subplots(figsize=(16, 9))
    plt.plot(values, label="Value")
    plt.plot(weights, label="Weight")
    plt.axhline(max_weight, label="Maximum Weight", c="black")
    plt.legend()
    plt.xlabel("Iteration")
    plt.savefig("results.png", bbox_index="tight")


def write_solution(solution, path):
    with open(path, 'w') as f:
        f.write(f"Total Value: {solution.value}\n")
        f.write(f"Total Weight: {solution.weight}\n")
        f.write("Item\tValue\tWeight\n")
        for i, p in enumerate(solution.packing):
            if p == 1:
                f.write(f"{i}\t{solution.values[i]}\t{solution.weights[i]}\n")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("path", help="Path to the data file")
    parser.add_argument("max_w", help="Maximum weight constraint", type=int)
    args = parser.parse_args()
    values, weights = parse_data(args.path)
    max_weight = args.max_w

    ks = SimulatedAnnealing(values, weights, max_weight)
    solution, v_hist, w_hist = ks.optimize()
    plot_results(v_hist, w_hist, max_weight)
    write_solution(solution, "solution.txt")
