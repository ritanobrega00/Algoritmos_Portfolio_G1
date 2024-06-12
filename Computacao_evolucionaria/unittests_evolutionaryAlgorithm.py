import unittest
import random
import numpy as np
from Individual import Individual
from Population import Population
from EvolAlgorithmReal import EvolAlgorithmReal
from unittest.mock import MagicMock
from EvolAlgorithm import EvolAlgorithm, Individual


class TestIndividuos(unittest.TestCase):
    def test_init(self):
        indiv = Individuos(5, 1, 0)
        self.assertEqual(len(indiv.genome), 5)
        self.assertTrue(all(0 <= gene <= 1 for gene in indiv.genome))

    def test_mutation(self):
        indiv = Individuos(5, 1, 0, [0, 1, 1, 0, 1])
        original_genome = indiv.genome[:]
        indiv.mutation()
        self.assertNotEqual(indiv.genome, original_genome)

    def test_crossover(self):
        parent1 = Individuos(5, 1, 0, [1, 1, 1, 1, 1])
        parent2 = Individuos(5, 1, 0, [0, 0, 0, 0, 0])
        child1, child2 = parent1.crossover(parent2)
        self.assertEqual(len(child1.genome), 5)
        self.assertEqual(len(child2.genome), 5)

    def test_crossover_multi(self):
        parent1 = Individuos(5, 1, 0, [1, 1, 1, 1, 1])
        parent2 = Individuos(5, 1, 0, [0, 0, 0, 0, 0])
        child1, child2 = parent1.crossover_multi(parent2, 2)
        self.assertEqual(len(child1.genome), 5)
        self.assertEqual(len(child2.genome), 5)

    def test_get_fitness(self):
        indiv = Individuos(5, 1, 0, [1, 0, 1, 0, 1])
        self.assertEqual(indiv.get_fitness(), 3)

class TestPopulation(unittest.TestCase):

    def setUp(self):
        """Configuração para os testes."""
        self.pop_size = 10
        self.indiv_length = 5
        self.lower_bound = 0
        self.upper_bound = 1
        self.population = Population(self.pop_size, self.indiv_length, self.lower_bound, self.upper_bound)

    def test_population_initialization(self):
        """Teste para verificar a inicialização da população."""
        self.assertEqual(len(self.population.indivs), self.pop_size)
        for indiv in self.population.indivs:
            self.assertEqual(len(indiv.genome), self.indiv_length)
            for gene in indiv.genome:
                self.assertGreaterEqual(gene, self.lower_bound)
                self.assertLessEqual(gene, self.upper_bound)

    def test_get_indiv(self):
        """Teste para verificar a obtenção de um indivíduo pelo índice."""
        indiv = self.population.get_indiv(0)
        self.assertIsInstance(indiv, Individual)
        self.assertEqual(len(indiv.genome), self.indiv_length)

    def test_get_fitnesses(self):
        """Teste para verificar a obtenção das aptidões dos indivíduos."""
        fitnesses = self.population.get_fitnesses()
        self.assertEqual(len(fitnesses), self.pop_size)
        for fitness in fitnesses:
            self.assertIsInstance(fitness, float)

    def test_best_indiv(self):
        """Teste para verificar a obtenção do melhor indivíduo."""
        best_indiv = self.population.best_indiv()
        self.assertIsInstance(best_indiv, Individual)
        best_fitness = best_indiv.evaluate_fitness()
        for indiv in self.population.indivs:
            self.assertGreaterEqual(best_fitness, indiv.evaluate_fitness())

    def test_best_fitness(self):
        """Teste para verificar a obtenção da melhor aptidão."""
        best_fitness = self.population.best_fitness()
        self.assertIsInstance(best_fitness, float)
        for indiv in self.population.indivs:
            self.assertGreaterEqual(best_fitness, indiv.evaluate_fitness())

    def test_selection(self):
        """Teste para verificar a seleção de indivíduos."""
        selected = self.population.selection(4)
        self.assertEqual(len(selected), 4)
        for indiv in selected:
            self.assertIsInstance(indiv, Individual)

    def test_recombination(self):
        """Teste para verificar a recombinação de indivíduos."""
        selected = self.population.selection(4)
        offspring = self.population.recombination(selected, 4)
        self.assertEqual(len(offspring), 4)
        for indiv in offspring:
            self.assertIsInstance(indiv, Individual)
            self.assertEqual(len(indiv.genome), self.indiv_length)

    def test_reinsertion(self):
        """Teste para verificar a reinserção de descendentes na população."""
        selected = self.population.selection(4)
        offspring = self.population.recombination(selected, 4)
        self.population.reinsertion(offspring)
        self.assertEqual(len(self.population.indivs), self.pop_size)
        for indiv in self.population.indivs:
            self.assertIsInstance(indiv, Individual)

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
        mutate(individual, 1.0, 0.0, 10.0)
        self.assertNotEqual(individual.genome, original_genome)
        self.assertTrue(all(0.0 <= gene <= 10.0 for gene in individual.genome))


class MockIndividual(Individual):
    def __init__(self, genome_length, lower_bound, upper_bound):
        super().__init__(genome_length, lower_bound, upper_bound)
        self.fitness = None  # Mocked attribute for fitness

class TestEvolAlgorithm(unittest.TestCase):
    def setUp(self):
        self.population_size = 10
        self.genome_length = 5
        self.lower_bound = 0.0
        self.upper_bound = 1.0
        self.mutation_rate = 0.1
        self.max_generations = 20
        self.original_individual_class = EvolAlgorithm.Individual
        EvolAlgorithm.Individual = MockIndividual

        self.ea = EvolAlgorithm(self.population_size, self.genome_length, self.lower_bound,
                                self.upper_bound, self.mutation_rate, self.max_generations)

    def tearDown(self):
        EvolAlgorithm.Individual = self.original_individual_class

    def test_initialize_population(self):
        population = self.ea.inicializar_populacao()
        self.assertEqual(len(population), self.population_size)
        for individual in population:
            self.assertEqual(len(individual.genome), self.genome_length)
            for gene in individual.genome:
                self.assertGreaterEqual(gene, self.lower_bound)
                self.assertLessEqual(gene, self.upper_bound)

    def test_avaliar(self):
        self.ea.avaliar = MagicMock()

        individual = MockIndividual(self.genome_length, self.lower_bound, self.upper_bound)
        self.ea.avaliar(individual)
        self.assertTrue(self.ea.avaliar.called)
        self.assertIsNotNone(individual.fitness)

    def test_selecionar_pais(self):
        fitness_values = [random.uniform(0, 1) for _ in range(self.population_size)]
        for individual, fitness in zip(self.ea.populacao, fitness_values):
            individual.fitness = fitness

        pais = self.ea.selecionar_pais()
        self.assertEqual(len(pais), 2)
        self.assertIsInstance(pais[0], MockIndividual)
        self.assertIsInstance(pais[1], MockIndividual)

    def test_crossover(self):
        parent1 = MockIndividual(self.genome_length, self.lower_bound, self.upper_bound)
        parent2 = MockIndividual(self.genome_length, self.lower_bound, self.upper_bound)
        child1, child2 = self.ea.crossover(parent1, parent2)

        self.assertEqual(len(child1.genome), self.genome_length)
        self.assertEqual(len(child2.genome), self.genome_length)
        self.assertNotEqual(child1.genome, parent1.genome)
        self.assertNotEqual(child2.genome, parent2.genome)

    def test_mutacao(self):
        random.seed(1)  
        original_random = random.random
        random.random = MagicMock(side_effect=lambda: 0.05)

        individual = MockIndividual(self.genome_length, self.lower_bound, self.upper_bound)
        original_genome = individual.genome[:]
        self.ea.mutacao(individual)

        random.random = original_random

        self.assertNotEqual(individual.genome, original_genome)
        for gene in individual.genome:
            self.assertGreaterEqual(gene, self.lower_bound)
            self.assertLessEqual(gene, self.upper_bound)

    def test_substituir_populacao(self):
        nova_populacao = [MockIndividual(self.genome_length, self.lower_bound, self.upper_bound) for _ in range(self.population_size)]
        self.ea.substituir_populacao(nova_populacao)
        self.assertEqual(self.ea.populacao, nova_populacao)


class TestEvolAlgorithmReal(unittest.TestCase):
    def setUp(self):
        self.sequences = ['ACGTACGT', 'CGTACGTA', 'TACGTACG']
        self.ea_real = EvolAlgorithmReal(10, 5, 4, self.sequences)

    def test_construct_pwm(self):
        genome = np.array([
            [0.1, 0.2, 0.3, 0.4],
            [0.4, 0.3, 0.2, 0.1],
            [0.3, 0.3, 0.2, 0.2],
            [0.2, 0.2, 0.3, 0.3],
            [0.5, 0.2, 0.1, 0.2]
        ])
        pwm = self.ea_real.construct_pwm(genome)
        self.assertEqual(pwm.shape, (5, 4))
        self.assertTrue(np.array_equal(pwm, genome))

    def test_normalize_pwm(self):
        pwm = np.array([
            [1.0, 2.0, 3.0, 4.0],
            [0.4, 0.3, 0.2, 0.1],
            [0.3, 0.3, 0.2, 0.2],
            [0.2, 0.2, 0.3, 0.3],
            [0.5, 0.2, 0.1, 0.2]
        ])
        normalized_pwm = self.ea_real.normalize_pwm(pwm)
        expected_normalized_pwm = np.array([
            [0.1, 0.2, 0.3, 0.4],
            [0.4/1.0, 0.3/1.0, 0.2/1.0, 0.1/1.0],
            [0.3/1.0, 0.3/1.0, 0.2/1.0, 0.2/1.0],
            [0.2/1.0, 0.2/1.0, 0.3/1.0, 0.3/1.0],
            [0.5/1.0, 0.2/1.0, 0.1/1.0, 0.2/1.0]
        ])
        np.testing.assert_almost_equal(normalized_pwm, expected_normalized_pwm)

    def test_find_max_prob_position(self):
        pwm = np.array([
            [0.1, 0.2, 0.3, 0.4],
            [0.4, 0.3, 0.2, 0.1],
            [0.3, 0.3, 0.2, 0.2],
            [0.2, 0.2, 0.3, 0.3],
            [0.5, 0.2, 0.1, 0.2]
        ])
        sequence = 'ACGTACGT'
        max_prob_position = self.ea_real.find_max_prob_position(pwm, sequence)
        self.assertEqual(max_prob_position, 0)

    def test_calculate_sequence_probability(self):
        pwm = np.array([
            [0.1, 0.2, 0.3, 0.4],
            [0.4, 0.3, 0.2, 0.1],
            [0.3, 0.3, 0.2, 0.2],
            [0.2, 0.2, 0.3, 0.3],
            [0.5, 0.2, 0.1, 0.2]
        ])
        subsequence = 'ACGT'
        prob = self.ea_real.calculate_sequence_probability(pwm, subsequence)
        expected_prob = 0.1 * 0.3 * 0.2 * 0.2
        self.assertAlmostEqual(prob, expected_prob)

    def test_calculate_fitness(self):
        s_vector = [0, 1, 2]
        fitness = self.ea_real.calculate_fitness(s_vector)
        self.assertAlmostEqual(fitness, 3.0)

if __name__ == '__main__':
    unittest.main()
