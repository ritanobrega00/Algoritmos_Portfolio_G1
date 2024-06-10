from Individual import Individual
import random

class Population:
    def __init__(self, size, indiv_length, lower_bound, upper_bound):
        self.size = size
        self.indiv_length = indiv_length
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.population = []

    def init_random_pop(self):
        self.population = [Individual(self.indiv_length, self.lower_bound, self.upper_bound) for _ in range(self.size)]

if __name__ == "__main__": 
    teste()