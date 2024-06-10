import unittest
import random
import numpy as np
from evolutionary_code import Individual, crossover, mutate, Popul, IndivReal, PopulReal, EvolAlgorithm, EvolAlgorithmReal

class TestIndividual(unittest.TestCase):
    def test_init(self):
        individual = Individual(5, 0.0, 10.0)
        self.assertEqual(len(individual.genome), 5)
        self.assertTrue(all(0.0 <= gene <= 10.0 for gene in individual.genome))

    def test_evaluate_fitness(self):
        individual = Individual(5, 0.0, 10.0)
        individual.genome = [1, 2, 3, 4, 5]
        individual.evaluate_fitness()
        self.assertEqual(individual.fitness, 1**2 + 2**2 + 3**2 + 4**2 + 5**2)

class TestCrossover(unittest.TestCase):
    def test_crossover(self):
        parent1 = Individual(5, 0.0, 10.0)
        parent2 = Individual(5, 0.0, 10.0)
        child1, child2 = crossover(parent1, parent2, 0.0, 10.0)
        self.assertEqual(len(child1.genome), 5)
        self.assertEqual(len(child2.genome), 5)
        self.assertTrue(all(0.0 <= gene <= 10.0 for gene in child1.genome))
        self.assertTrue(all(0.0 <= gene <= 10.0 for gene in child2.genome))

class TestMutate(unittest.TestCase):
    def test_mutate(self):
        individual = Individual(5, 0.0, 10.0)
        original_genome = individual.genome[:]
        mutate(individual, 1.0, 0.0, 10.0)  # mutation_rate = 1.0 ensures mutation
        self.assertNotEqual(individual.genome, original_genome)
        self.assertTrue(all(0.0 <= gene <= 10.0 for gene in individual.genome))

class TestPopul(unittest.TestCase):
    def test_init_random_pop(self):
        population = Popul(10, 5, 0.0, 10.0)
        population.init_random_pop()
        self.assertEqual(len(population.population), 10)
        for individual in population.population:
            self.assertEqual(len(individual.genome), 5)
            self.assertTrue(all(0.0 <= gene <= 10.0 for gene in individual.genome))

class TestIndivReal(unittest.TestCase):
    def test_init_random(self):
        individual = IndivReal(5, 0.0, 1.0)
        self.assertEqual(len(individual.genome), 5)
        self.assertTrue(all(0.0 <= gene <= 1.0 for gene in individual.genome))

class TestPopulReal(unittest.TestCase):
    def test_init_random_pop(self):
        population = PopulReal(10, 5, 0.0, 1.0)
        population.init_random_pop()
        self.assertEqual(len(population.population), 10)
        for individual in population.population:
            self.assertEqual(len(individual.genome), 5)
            self.assertTrue(all(0.0 <= gene <= 1.0 for gene in individual.genome))

class TestEvolAlgorithm(unittest.TestCase):
    def test_run(self):
        algorithm = EvolAlgorithm(10, 5, 0.0, 10.0, 0.1, 2)
        algorithm.run()
        self.assertEqual(len(algorithm.population), 10)
        for individual in algorithm.population:
            self.assertIsNotNone(individual.fitness)

class TestEvolAlgorithmReal(unittest.TestCase):
    def test_evaluate(self):
        sequences = ["ACGTACGTGAC", "GTCACGTACGT", "TACGTACGTGA"]
        algorithm = EvolAlgorithmReal(10, 3, 4, sequences)
        individual = algorithm.population[0]
        algorithm.evaluate(individual)
        self.assertIsNotNone(individual.fitness)

if __name__ == '__main__':
    unittest.main()
