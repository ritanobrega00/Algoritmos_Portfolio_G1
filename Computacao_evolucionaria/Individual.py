import random

class Individual:
    def __init__(self, length, lower_bound, upper_bound):
        self.genome = [random.uniform(lower_bound, upper_bound) for _ in range(length)]
        self.fitness = None

    def evaluate_fitness(self):
        self.fitness = sum(x**2 for x in self.genome)

if __name__ == "__main__": 
    teste()