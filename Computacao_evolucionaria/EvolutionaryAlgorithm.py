from Population import Population
from Individual import Individual
import random

class EvolAlgorithmReal(EvolAlgorithm):
    def __init__(self, population_size, motif_length, alphabet_size, sequences):
        self.motif_length = motif_length
        self.alphabet_size = alphabet_size
        self.sequences = sequences
        super().__init__(population_size, motif_length * alphabet_size, 0.0, 1.0, 0.1, 20)

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
        column_sums = np.sum(pwm, axis=1)
        normalized_pwm = pwm / column_sums[:, np.newaxis]
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
            symbol_index = ord(symbol) - ord('A')
            prob *= pwm[i, symbol_index]
        return prob

    def calculate_fitness(self, s_vector):
        position_sum = sum(s_vector)
        dispersion_penalty = np.std(s_vector)
        return position_sum - dispersion_penalty


if __name__ == "__main__": 
    teste()