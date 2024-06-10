import unittest
from EvolutionaryAlgorithm import EvolutionaryAlgorithm
from EvolutionaryAlgorithmReal import EvolutionaryAlgorithmReal

class TestEvolutionaryAlgorithm(unittest.TestCase):

    def test_EvolutionaryAlgorithm(self):
        population_size = 10
        genome_length = 5
        lower_bound = 0.0
        upper_bound = 10.0
        mutation_rate = 0.1
        generations = 20

        evol_algorithm = EvolutionaryAlgorithm(population_size, genome_length, lower_bound, upper_bound, mutation_rate, generations)
        evol_algorithm.run()

    def test_EvolutionaryAlgorithmReal(self):
        sequences = ["ACGTACGTGAC", "GTCACGTACGT", "TACGTACGTGA"]
        motif_length = 3
        alphabet_size = 4
        population_size = 10

        evol_algorithm_real = EvolutionaryAlgorithmReal(population_size, motif_length, alphabet_size, sequences)
        evol_algorithm_real.run()

if __name__ == '__main__':
    unittest.main()