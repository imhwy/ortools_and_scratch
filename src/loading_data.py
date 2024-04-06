import os
from tqdm import tqdm


class LoadingData:
    def __init__(self, folder_path, file_name):
        self.folder_path = folder_path
        self.file_name = file_name
        self.data = list()

    def get_data(self):
        with open(f"{self.folder_path}/{self.file_name}", 'r', encoding='utf-8') as f:
            self.data = f.readlines()

    def load_data_for_ortools(self):
        max_capacity = int(self.data[2])
        values = []
        weights = []
        for line in self.data[4:]:
            line_values = line.split()
            values.append(int(line_values[0]))
            weights.append(int(line_values[1]))
        weights = [weights]
        capacities = [max_capacity]
        return values, weights, capacities

    def load_data_for_scratch(self):
        max_capacity = int(self.data[2])
        values = []
        weights = []
        for line in self.data[4:]:
            line_values = line.split()
            values.append(int(line_values[0]))
            weights.append(int(line_values[1]))
        weights = weights
        capacities = max_capacity
        return values, weights, capacities
