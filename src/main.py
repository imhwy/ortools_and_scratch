from ortools_module import *
from scratch_module import *
from loading_data import *
import time


def main():
    # loading data
    folder_path = "../data"
    for file_name in tqdm(os.listdir(folder_path)):
        data_loader = LoadingData(folder_path, file_name)
        data_loader.get_data()
        values, weights, capacities = data_loader.load_data_for_scratch()
        solver_scratch = ScratchSolver(values, weights, capacities)
        print(f"===================={file_name}====================")
        greedy_start_time = time.time()
        greedy_value = solver_scratch.knapsack_greedy()
        greedy_end_time = time.time()
        greedy_execute_time = greedy_end_time - greedy_start_time
        print("Best value of Greedy algorithm: ", greedy_value)
        print("Execute time of Greedy algorithm",
              "{:.10f}".format(greedy_execute_time))
        print(f"====================")
        # bruteforce_start_time = time.time()
        # bruteforce_value = solver_scratch.knapsack_bruteforce()
        # bruteforce_end_time = time.time()
        # bruteforce_execute_time = bruteforce_end_time - bruteforce_start_time
        # print("Best value of bruteforce algorithm: ", bruteforce_value)
        # print("Execute time of bruteforce algorithm", bruteforce_execute_time)
        # print(f"====================")
        dynamic_programming_start_time = time.time()
        dynamic_programming_value = solver_scratch.knapsack_dynamic_programming()
        dynamic_programming_end_time = time.time()
        dynamic_programming_execute_time = dynamic_programming_end_time - \
            dynamic_programming_start_time
        print("Best value of dynamic_programming algorithm: ",
              dynamic_programming_value)
        print("Execute time of dynamic_programming algorithm",
              dynamic_programming_execute_time)


if __name__ == "__main__":
    main()
