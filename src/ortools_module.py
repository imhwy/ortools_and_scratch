# import libraries
from ortools.algorithms.python import knapsack_solver

class OrtoolSolver:
    def __init__(self, solver, values, weights, capacities):
        self.values = values
        self.weights = weights
        self.capacities = capacities
        self.solver = solver

    def solve_knapsack(self):
        self.solver.init(self.values, self.weights, self.capacities)
        computed_value = self.solver.solve()
        return computed_value
    
    def packed_weights(self):
        packed_items = []
        packed_weights = []
        total_weight = 0
        for i in range(len(self.values)):
            if self.solver.best_solution_contains(i):
                packed_items.append(i)
                packed_weights.append(self.weights[0][i])
                total_weight += self.weights[0][i]
        return total_weight
    