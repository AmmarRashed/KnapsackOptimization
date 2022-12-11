import numpy as np
from copy import deepcopy


def flip_bit(bit):
    return abs(bit - 1)


class Solution:
    def __init__(self, packing, values, weights, max_weight):
        self.packing = packing
        self.values = values
        self.weights = weights
        self.max_weight = max_weight

        self.n = len(self.packing)

        self.value, self.weight = None, None
        self.update_objective()

    def update_objective(self):
        v = 0
        w = 0
        for i, p in enumerate(self.packing):
            v += self.values[i] * p
            w += self.weights[i] * p
        self.value = -1 if w > self.max_weight else v
        self.weight = w

    def adjacent(self):
        new = self.packing.copy()
        # if knapsack is at maximum weight or more, try removing an item
        if self.weight >= self.max_weight:
            idx = np.random.choice(np.where(new == True)[0])
        else:
            idx = np.random.choice(np.arange(self.n))
        new[idx] = flip_bit(new[idx])  # flip the bit
        return Solution(new, self.values, self.weights, self.max_weight)

    def flip(self, i):
        self.packing[i] = flip_bit(self.packing[i])
        self.update_objective()

    def __copy__(self):
        return deepcopy(self)

    def copy(self):
        return self.__copy__()


class Knapsack:
    def __init__(self, values, weights, max_weight):
        """
        Args:
            values: list of item values
            weights: list of item weights
            max_weight: maximum weight allowed
        """
        self.values = values
        self.weights = weights
        self.max_weight = max_weight

        self.n = len(self.values)  # number of items

    def optimize(self, *args, **kwargs):
        pass
