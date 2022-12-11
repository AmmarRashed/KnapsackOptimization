from base import *
from greedy import Greedy


class TabuSearch(Knapsack):
    def optimize(self, tenure=100):
        # begin with a starting current solution
        best, _, _ = Greedy(self.values, self.weights, self.max_weight).optimize()

        T = []
        iteration = 0
        best_iteration = 0

        while best_iteration - iteration <= tenure:  # how many iterations since the best solution has been found
            iteration += 1
            solution_tabu = list()
            for i in range(self.n):
                temp.flip(i)
                solution_partial = temp.copy()
                if solution_partial.value > valor and i not in T:
                    save_solution = solution_partial.copy()
                    valor = save_solution.value
                    mov = i
                    if solution_partial.value > best.value:
                        best = solution_partial.copy()
                        best_iteration = iteration
                elif solution_partial.value > best.value:
                    save_solution = solution_partial.copy()
                    valor = save_solution.value
                    best = solution_partial.copy()
                    best_iteration = iteration
                    mov = i
                elif i in T and solution_partial.value > valor_tabu:
                    solution_tabu = solution_partial.copy()
                    valor_tabu = solution_tabu.value
                    mov_tabu = i

                temp.flip(i)
            if mov == -1 and mov_tabu == -1:
                break
            if mov != -1:
                if mov not in T:
                    if len(T) == 3:
                        del T[0]
                    T.append(mov)
                temp = save_solution.copy()
            else:
                temp = solution_tabu.copy()
        return best
