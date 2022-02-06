import numpy as np

from base import Knapsack, Solution


class SimulatedAnnealing(Knapsack):

    def optimize(self, n_iterations=500, initial_temp=1000, cooling_rate=0.98, min_temp=1e-4):
        """

        Args:
            n_iterations: maximum number of iterations before halting the algorithm
            initial_temp: Starting temperature
            cooling_rate: Multiply the temperature by this rate after each iteration
            min_temp: minimum temperature value

        Returns:
            A list of the items picked in the optimum packing solution
        """

        # initial solution by randomly adding 25% of the items in the knapsack
        current = Solution(np.random.rand(self.n) < 0.25,
                           self.values, self.weights, self.max_weight)
        best = current

        temp = initial_temp
        for i in range(n_iterations):
            candidate = current.adjacent()  # candidate solution
            delta = candidate.value - current.value
            if candidate.value >= best.value:
                best = candidate
                current = candidate
            elif delta >= 0:
                current = candidate
            elif np.random.rand() < np.exp(delta / temp):
                current = candidate
            temp = max(temp * cooling_rate, min_temp)
        return best
