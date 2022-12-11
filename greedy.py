import numpy as np

from base import Knapsack, Solution


class Greedy(Knapsack):

    def optimize(self, n_iterations=500):
        """

        Args:
            n_iterations: maximum number of iterations before halting the algorithm

        Returns:
            A list of the items picked in the optimum packing solution
        """

        # initial solution by randomly adding 25% of the items in the knapsack
        best = Solution(np.random.rand(self.n) < 0.25,
                        self.values, self.weights, self.max_weight)

        val_hist = []
        weight_hist = []
        for i in range(n_iterations):
            candidate = best.adjacent()  # candidate solution
            if candidate.value >= best.value:
                best = candidate
            val_hist.append(best.value)
            weight_hist.append(best.weight)
        return best, val_hist, weight_hist
