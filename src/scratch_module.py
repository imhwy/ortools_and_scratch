class ScratchSolver:
    def __init__(self, values, weights, capacities):
        self.values = values
        self.weights = weights
        self.capacities = capacities

    def knapsack_greedy(self):
        n = len(self.values)
        value_per_weight = [(self.values[i] / self.weights[i], i)
                            for i in range(n)]
        value_per_weight.sort(reverse=True)
        total_value = 0
        total_weight = 0
        selected_items = []
        for vpw, index in value_per_weight:
            if total_weight + self.weights[index] <= self.capacities:
                total_value += self.values[index]
                total_weight += self.weights[index]
                selected_items.append(index)
        return total_value

    def knapsack_bruteforce(self):
        n = len(self.values)

        def subset_value_weight(subset):
            total_value = sum(self.values[i] for i in subset)
            total_weight = sum(self.weights[i] for i in subset)
            return total_value, total_weight

        def generate_subsets(index, subset):
            if index == n:
                return subset
            include_subset = generate_subsets(index + 1, subset + [index])
            exclude_subset = generate_subsets(index + 1, subset)
            include_value, include_weight = subset_value_weight(include_subset)
            exclude_value, exclude_weight = subset_value_weight(exclude_subset)
            if include_weight <= self.capacities and include_value > exclude_value:
                return include_subset
            else:
                return exclude_subset
        best_subset = generate_subsets(0, [])
        best_value, best_weight = subset_value_weight(best_subset)
        return best_value

    def knapsack_dynamic_programming(self):
        n = len(self.values)
        dp = [[0] * (self.capacities + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for w in range(1, self.capacities + 1):
                if self.weights[i - 1] <= w:
                    dp[i][w] = max(dp[i - 1][w], dp[i - 1][w -
                                   self.weights[i - 1]] + self.values[i - 1])
                else:
                    dp[i][w] = dp[i - 1][w]
        selected_items = []
        w = self.capacities
        for i in range(n, 0, -1):
            if dp[i][w] != dp[i - 1][w]:
                selected_items.append(i - 1)
                w -= self.weights[i - 1]
        return dp[n][self.capacities]
