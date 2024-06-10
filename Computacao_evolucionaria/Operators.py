import random
from Individual import Individual

def crossover(parent1, parent2, lower_bound, upper_bound):
    child1_genome = []
    child2_genome = []
    for g1, g2 in zip(parent1.genome, parent2.genome):
        alpha = random.random()
        child1_genome.append(alpha * g1 + (1 - alpha) * g2)
        child2_genome.append(alpha * g2 + (1 - alpha) * g1)
    child1 = Individual(len(child1_genome), lower_bound, upper_bound)
    child2 = Individual(len(child2_genome), lower_bound, upper_bound)
    child1.genome = child1_genome
    child2.genome = child2_genome
    return child1, child2

def mutate(individual, mutation_rate, lower_bound, upper_bound):
    for i in range(len(individual.genome)):
        if random.random() < mutation_rate:
            individual.genome[i] += random.gauss(0, 1)
            individual.genome[i] = max(lower_bound, min(individual.genome[i], upper_bound))

if __name__ == "__main__": 
    teste()