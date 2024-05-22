from EvolAlgorithm import EvolAlgorithm
from Popul import PopulInt, PopulReal
from MotifFinding import MotifFinding
from MyMotifs import MyMotifs



def create_matrix_zeros(nrows, ncols):
    """
    Cria uma matriz com o número de linhas e colunas especificado, preenchida com zeros.

    Parâmetros:
    nrows (int): Número de linhas na matriz.
    ncols (int): Número de colunas na matriz.

    Retorna:
    list[list[int]]: Uma matriz preenchida com zeros.
    """
    return [[0] * ncols for _ in range(nrows)]

def print_matrix(mat):
    """
    Imprime a matriz fornecida de forma mais legível.

    Parâmetros:
    mat (list[list[int]]): A matriz a ser impressa.
    """
    for row in mat:
        print(' '.join(str(x) for x in row))



from typing import List

class MyMotifs:
    """Classe para manipular a matriz de pesos probabilística (PWM)"""

    def __init__(self, seqs: List[str] = [], pwm: List[List[float]] = [], alphabet: List[str] = None):
        """
        Inicia a classe MyMotifs.
        
        Parâmetros:
        seqs (List[str]): Lista de sequências de DNA/RNA.
        pwm (List[List[float]]): matriz de pesos probabilística (PWM).
        alphabet (List[str]): Alfabeto das sequências (['A', 'C', 'G', 'T']).

        Quando a sequeência é fornecida, a PWM é criada a partir das contagens das bases. Caso isto não aconteça, a PWM fornecida é usada diretamente.
        """
        self.seqs = seqs
        self.alphabet = alphabet or self.get_alphabet()
        self.size = len(self.seqs[0]) if seqs else len(pwm[0])

        if seqs:
            self.compute_counts()  # Calcula quantas vezes cada base em cada posição (counts) aparece nas sequências fornecidas para criar a PWM
            self.create_pwm()  # Cria a PWM a partir das counts
        else:
            self.pwm = pwm  # Se a PWM for fornecida como argumento ao criar uma instância da classe MyMotifs, essa PWM é utilizada diretamente em vez de ser calculada a partir das sequências.


    def get_alphabet(self) -> List[str]:
        """
        Retorna:
        List[str]: Lista de caracteres únicos na primeira sequência.
        """
        return list(set(self.seqs[0]))  # Converte a sequência num conjunto para obter caracteres únicos e depois numa lista


    @property
    def pwm(self) -> List[List[float]]:
         """
        Retorna a PWM
        """
        return self._pwm


    @pwm.setter
    def pwm(self, value: List[List[float]]):
        """
        Define a PWM e atualiza o tamanho.
        """
        self._pwm = value
        self.size = len(value[0])  # Atualiza o tamanho baseado na PWM


    def compute_counts(self):
        """
        Computa as counts para cada posição nas sequências.

        Este método cria uma matriz de counts onde cada linha representa uma base e
        cada coluna representa uma posição na sequência.
        """
        self.counts = [[0] * self.size for _ in range(len(self.alphabet))]
        for seq in self.seqs:
            for i, letter in enumerate(seq):
                lin = self.alphabet.index(letter)
                self.counts[lin][i] += 1

    def create_pwm(self):
        """Cria a Matriz de Pesos Probabilística (PWM) a partir das contagens de letras"""
        if self.counts is None:
            self.compute_counts()  # Garante que as contagens estão computadas

        self.pwm = [[float(count) / sum(col) for count in col] for col in zip(*self.counts)]

    def __len__(self) -> int:
        return self.size

    def consensus(self) -> str:
        """Retorna o motivo de sequência obtido com o símbolo mais frequente em cada posição do motivo."""
        result = ""
        for position in range(self.size):
            max_count = self.counts[0][position]
            max_count_index = 0
            for index in range(1, len(self.alphabet)):
                if self.counts[index][position] > max_count:
                    max_count = self.counts[index][position]
                    max_count_index = index
            result += self.alphabet[max_count_index]
        return result

    def masked_consensus(self) -> str:
        """Retorna o motivo de sequência obtido com o símbolo que ocorre em pelo menos 50% das sequências de entrada."""
        result = ""
        for position in range(self.size):
            max_count = self.counts[0][position]
            max_count_index = 0
            for index in range(1, len(self.alphabet)):
                if self.counts[index][position] > max_count:
                    max_count = self.counts[index][position]
                    max_count_index = index
            if max_count > len(self.seqs) / 2:
                result += self.alphabet[max_count_index]
            else:
                result += "-"
        return result

    def probability_sequence(self, seq: str) -> float:
        """Calcula a probabilidade da sequência fornecida com base na matriz de pesos posicional (PWM)."""
        result = 1.0
        for position in range(self.size):
            index = self.alphabet.index(seq[position])
            result *= self.pwm[index][position]
        return result

    def probability_all_positions(self, seq: str) -> List[float]:
        """Calcula a probabilidade de todas as subsequências possíveis da sequência fornecida."""
        result = []
        for position in range(len(seq) - self.size + 1):
            result.append(self.probability_sequence(seq[position:position + self.size]))
        return result

    def most_probable_sequence(self, seq: str) -> int:
        """Retorna o índice da subsequência mais provável da sequência de entrada."""
        maximum = -1.0
        max_index = -1
        for position in range(len(seq) - self.size + 1):
            probability = self.probability_sequence(seq[position:position + self.size])
            if probability > maximum:
                maximum = probability
                max_index = position
        return max_index

    def create_motif(self, seqs: List['MySeq']) -> 'MyMotifs':
        """Cria um motivo a partir de uma lista de sequências."""
        from MySeq import MySeq
        result = []
        for sequence in seqs:
            index = self.most_probable_sequence(sequence.seq)
            subseq = MySeq(sequence.seq[index:index + self.size], sequence.get_seq_biotype())
            result.append(subseq)
        return MyMotifs(result)







import random

# Definição da classe Individual com representação real
class Individual:
    def __init__(self, length, lower_bound, upper_bound):
        self.genome = [random.uniform(lower_bound, upper_bound) for _ in range(length)]
        self.fitness = None

    def evaluate_fitness(self):
        # Defina aqui a função de avaliação de fitness adequada ao seu problema
        self.fitness = sum(self.genome)  # Exemplo simplificado: soma dos genes

# Função de cruzamento (crossover) aritmético
def crossover(parent1, parent2):
    child1_genome = []
    child2_genome = []
    for g1, g2 in zip(parent1.genome, parent2.genome):
        alpha = random.random()  # Fator de cruzamento
        child1_genome.append(alpha * g1 + (1 - alpha) * g2)
        child2_genome.append(alpha * g2 + (1 - alpha) * g1)
    child1 = Individual(len(child1_genome), lower_bound, upper_bound)
    child2 = Individual(len(child2_genome), lower_bound, upper_bound)
    child1.genome = child1_genome
    child2.genome = child2_genome
    return child1, child2

# Função de mutação gaussiana
def mutate(individual, mutation_rate, lower_bound, upper_bound):
    for i in range(len(individual.genome)):
        if random.random() < mutation_rate:
            individual.genome[i] += random.gauss(0, 1)
            # Garantir que os valores permanecem dentro dos limites
            individual.genome[i] = max(lower_bound, min(individual.genome[i], upper_bound))

# Parâmetros
population_size = 10
genome_length = 5
lower_bound = 0.0
upper_bound = 10.0
mutation_rate = 0.1
generations = 20

# Inicialização da população
population = [Individual(genome_length, lower_bound, upper_bound) for _ in range(population_size)]

# Algoritmo evolutivo simplificado
for generation in range(generations):
    # Avaliação da população
    for individual in population:
        individual.evaluate_fitness()

    # Seleção (simplificada: ordenar por fitness e selecionar os melhores)
    population.sort(key=lambda ind: ind.fitness, reverse=True)
    new_population = population[:population_size // 2]

    # Cruzamento
    while len(new_population) < population_size:
        parent1, parent2 = random.sample(new_population, 2)
        child1, child2 = crossover(parent1, parent2)
        new_population.append(child1)
        if len(new_population) < population_size:
            new_population.append(child2)

    # Mutação
    for individual in new_population:
        mutate(individual, mutation_rate, lower_bound, upper_bound)

    # Atualizar população
    population = new_population

    # Imprimir a melhor solução da geração
    best_individual = max(population, key=lambda ind: ind.fitness)
    print(f"Generation {generation}: Best Fitness = {best_individual.fitness}, Genome = {best_individual.genome}")

# Imprimir a melhor solução final
best_individual = max(population, key=lambda ind: ind.fitness)
print(f"Best Solution: Fitness = {best_individual.fitness}, Genome = {best_individual.genome}")






class Indiv:
    def __init__(self, length):
        self.genome = [0] * length
        self.fitness = None

    def evaluate_fitness(self):
        raise NotImplementedError("Este método deve ser implementado nas subclasses.")

class Popul:
    def __init__(self, size, indiv_length):
        self.size = size
        self.indiv_length = indiv_length
        self.population = []

    def initRandomPop(self):
        raise NotImplementedError("Este método deve ser implementado nas subclasses.")


import random

class IndivReal(Indiv):
    def __init__(self, length, lower_bound=0.0, upper_bound=1.0):
        super().__init__(length)
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.initRandom()

    def initRandom(self):
        self.genome = [random.uniform(self.lower_bound, self.upper_bound) for _ in range(len(self.genome))]

    def mutation(self):
        gene_to_mutate = random.randint(0, len(self.genome) - 1)
        self.genome[gene_to_mutate] = random.uniform(self.lower_bound, self.upper_bound)



class PopulReal(Popul):
    def __init__(self, size, indiv_length, lower_bound=0.0, upper_bound=1.0):
        super().__init__(size, indiv_length)
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.initRandomPop()

    def initRandomPop(self):
        self.population = [IndivReal(self.indiv_length, self.lower_bound, self.upper_bound) for _ in range(self.size)]




#   Exemplo de utilização da classe PopulReal

# Parâmetros
population_size = 10
genome_length = 5

# Inicialização da população real
popul_real = PopulReal(population_size, genome_length)

# Mostrar a população inicial
print("População inicial:")
for indiv in popul_real.population:
    print(indiv.genome)

# Realizar mutação em cada indivíduo
print("\nPopulação após mutação:")
for indiv in popul_real.population:
    indiv.mutation()
    print(indiv.genome)



import random
import numpy as np

class EvolAlgorithmReal(EvolAlgorithm):
    def __init__(self, population_size, motif_length, alphabet_size, sequences):
        self.motif_length = motif_length
        self.alphabet_size = alphabet_size
        self.sequences = sequences
        super().__init__(population_size, motif_length * alphabet_size)

    def initPopul(self):
        self.population = PopulReal(self.population_size, self.indiv_length)

    def evaluate(self, individual):
        pwm = self.construct_pwm(individual.genome)
        normalized_pwm = self.normalize_pwm(pwm)
        s_vector = self.most_probable_positions(normalized_pwm, self.sequences)
        fitness = self.calculate_fitness(s_vector)
        individual.fitness = fitness

    def construct_pwm(self, genome):
        pwm = np.array(genome).reshape((self.motif_length, self.alphabet_size))
        return pwm

    def normalize_pwm(self, pwm):
        column_sums = np.sum(pwm, axis=0)
        normalized_pwm = pwm / column_sums
        return normalized_pwm

    def most_probable_positions(self, pwm, sequences):
        positions = []
        for sequence in sequences:
            max_prob_position = self.find_max_prob_position(pwm, sequence)
            positions.append(max_prob_position)
        return positions

    def find_max_prob_position(self, pwm, sequence):
        max_prob = -1
        max_prob_position = 0
        for i in range(len(sequence) - self.motif_length + 1):
            subsequence = sequence[i:i + self.motif_length]
            prob = self.calculate_sequence_probability(pwm, subsequence)
            if prob > max_prob:
                max_prob = prob
                max_prob_position = i
        return max_prob_position

    def calculate_sequence_probability(self, pwm, subsequence):
        prob = 1.0
        for i, symbol in enumerate(subsequence):
            symbol_index = ord(symbol) - ord('A')  # Assuming 'A' is the first symbol
            prob *= pwm[i, symbol_index]
        return prob

    def calculate_fitness(self, s_vector):
        # Implemente aqui o cálculo do score ou fitness baseado nos vetores s
        # Exemplo simples: fitness é a soma das posições mais prováveis do motif em cada sequência
        return sum(s_vector)
