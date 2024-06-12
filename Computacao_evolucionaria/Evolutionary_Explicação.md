Class EvolAlgorithm:
This class implements a framework for evolutionary algorithms. It facilitates the evolution of a population of individuals over multiple generations. Its main functionalities include initializing the population, evaluating fitness, selecting parents using roulette wheel selection, performing crossover to create offspring, mutating individual genomes, and replacing the current population with a new one based on evolutionary operations.

* init(self, population_size, genome_length, lower_bound, upper_bound, mutation_rate, max_generations):
The constructor initializes parameters for the evolutionary algorithm, including population size, genome length, mutation rate, and the maximum number of generations. It also initializes the population of individuals with randomly generated genomes within specified lower and upper bounds.

* initialize_population(self):
Initializes the population with individuals randomly generated, each with a genome of a specific length and within defined lower and upper bounds.

* evaluate_population(self):
Evaluates the fitness of all individuals in the population. This typically involves calculating a performance or fitness measure for each individual based on their genomes and the specific problem being addressed.

* evaluate(self, individual):
An abstract method intended to be overridden by subclasses. It evaluates the fitness of a specific individual. The concrete implementation of this function varies depending on the problem and the specific formulation of fitness.

* select_parents(self):
Selects parent individuals using roulette wheel selection, where the probability of selecting each individual is proportional to its fitness. This allows fitter individuals to have a higher chance of being chosen as parents for the next generation.

* crossover(self, parent1, parent2):
Performs crossover between two parent individuals to produce two offspring. Crossover involves exchanging parts of the genomes of the parents, creating new genetic combinations that may capture advantageous traits from both parents.

* mutate(self, individual):
Mutates the genome of an individual based on a specified mutation rate. Mutation introduces random variations into the genomes of individuals, exploring new genetic possibilities that may enhance the adaptability of offspring as they evolve over generations.

* replace_population(self, new_population):
Replaces the current population with a new population of individuals. This occurs after creating a new generation of individuals through selection, crossover, and mutation. The new population typically consists of a selection of the fittest individuals from the previous generation, combined with the offspring produced.

* run(self):
Executes the evolutionary algorithm over a maximum number of predefined generations. For each generation, the algorithm evaluates the fitness of the current population, creates a new population through evolutionary operations, replaces the old population with the new one, and optionally prints the fitness of the best individual in that generation.