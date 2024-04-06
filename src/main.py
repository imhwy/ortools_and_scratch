from ortools_module import *
from scratch_module import *
from loading_data import *

def main():
    # loading data
    folder_path = "../data"
    for file_name in tqdm(os.listdir(folder_path)):
        data_loader = LoadingData(folder_path, file_name)
        data_loader.get_data()
        # ortool implement
        values, weights, capacities = data_loader.load_data_for_ortools()
        # solver_bruteforce = knapsack_solver.KnapsackSolver(
        #     knapsack_solver.SolverType.KNAPSACK_BRUTE_FORCE_SOLVER,
        #     "KnapsackExample",
        # )
        solver_dynamic = knapsack_solver.KnapsackSolver(
            knapsack_solver.SolverType.KNAPSACK_DYNAMIC_PROGRAMMING_SOLVER,
            "KnapsackExample",
        )
        # ortool_bruteforce = OrtoolSolver(solver_bruteforce, values, weights, capacities)
        ortool_dynamic = OrtoolSolver(solver_dynamic, values, weights, capacities)
        # print("ortool brutefore result: ",ortool_bruteforce.solve_knapsack())
        print("ortool dynamic result: ",ortool_dynamic.solve_knapsack())
        values, weights, capacities = data_loader.load_data_for_scratch()
        solver = ScratchSolver(values, weights, capacities)
        print("scratch greedy: ", solver.knapsack_greedy())
        # print("scratch bruteforce: ", solver.knapsack_bruteforce())
        print("scratch dynamic: ", solver.knapsack_dynamic_programming())

if __name__ == "__main__":
    main()