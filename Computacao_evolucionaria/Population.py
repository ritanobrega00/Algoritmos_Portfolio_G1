import random
from Individual import Individual

class Population:
    def __init__(self, pop_size: int, indiv_length: int, lower_bound: float, upper_bound: float, indivs: list = None):
        """
        Inicia um novo objeto Population.

        Parâmetros:
            pop_size (int): O número de indivíduos na população.
            indiv_length (int): O comprimento do genoma de cada indivíduo.
            lower_bound (float): O limite inferior para os valores do genoma.
            upper_bound (float): O limite superior para os valores do genoma.
            indivs (list): Lista de indivíduos. Se for None, inicia aleatoriamente.
        """
        self.pop_size = pop_size
        self.indiv_length = indiv_length
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.indivs = indivs if indivs else self.init_random_pop()

    def init_random_pop(self) -> list:
        """
        Inicia a população com indivíduos aleatórios.

        Retorna:
            list: Lista de indivíduos.
        """
        return [Individual(self.indiv_length, self.lower_bound, self.upper_bound) for _ in range(self.pop_size)]

    def get_indiv(self, index: int) -> Individual:
        """
        Retorna o indivíduo no índice especificado.

        Parâmetros:
            index (int): Índice do indivíduo.

        Retorna:
            Individual: O indivíduo no índice especificado.
        """
        return self.indivs[index]

    def get_fitnesses(self) -> list:
        """
        Retorna os valores de aptidão de todos os indivíduos na população.

        Retorna:
            list: Lista de valores de aptidão.
        """
        return [indiv.evaluate_fitness() for indiv in self.indivs]

    def best_indiv(self) -> Individual:
        """
        Retorna o melhor indivíduo na população.

        Retorna:
            Individual: O melhor indivíduo.
        """
        return max(self.indivs, key=lambda indiv: indiv.evaluate_fitness())

    def best_fitness(self) -> float:
        """
        Retorna a aptidão do melhor indivíduo na população.

        Retorna:
            float: O valor de aptidão do melhor indivíduo.
        """
        return self.best_indiv().evaluate_fitness()

    def selection(self, num_indivs: int) -> list:
        """
        Seleciona indivíduos da população usando seleção por roleta.

        Parâmetros:
            num_indivs (int): Número de indivíduos a selecionar.

        Retorna:
            list: Lista de indivíduos selecionados.
        """
        fitnesses = self.get_fitnesses()
        total_fitness = sum(fitnesses)
        selected = []

        for _ in range(num_indivs):
            rand_val = random.uniform(0, total_fitness)
            current_sum = 0
            for i, fitness in enumerate(fitnesses):
                current_sum += fitness
                if current_sum >= rand_val:
                    selected.append(self.indivs[i])
                    total_fitness -= fitness
                    fitnesses[i] = 0
                    break
        return selected

    def recombination(self, parents: list, num_offspring: int) -> list:
        """
        Gera descendentes através de crossover e mutação.

        Parâmetros:
            parents (list): Lista de indivíduos pais.
            num_offspring (int): Número de descendentes a serem gerados.

        Retorna:
            list: Lista de descendentes.
        """
        offspring = []
        while len(offspring) < num_offspring:
            parent1, parent2 = random.sample(parents, 2)
            crossover_point = random.randint(1, self.indiv_length - 1)
            child_genome1 = parent1.genome[:crossover_point] + parent2.genome[crossover_point:]
            child_genome2 = parent2.genome[:crossover_point] + parent1.genome[crossover_point:]

            child1 = Individual(self.indiv_length, self.lower_bound, self.upper_bound)
            child1.genome = child_genome1
            child1.evaluate_fitness()

            child2 = Individual(self.indiv_length, self.lower_bound, self.upper_bound)
            child2.genome = child_genome2
            child2.evaluate_fitness()

            offspring.append(child1)
            offspring.append(child2)
        return offspring[:num_offspring]

    def reinsertion(self, offspring: list) -> None:
        """
        Substitui os piores indivíduos por descendentes.

        Parâmetros:
            offspring (list): Lista de descendentes a serem inseridos.
        """
        self.indivs.extend(offspring)
        self.indivs.sort(key=lambda indiv: indiv.evaluate_fitness(), reverse=True)
        self.indivs = self.indivs[:self.pop_size]

if __name__ == "__main__":
    # Exemplo de uso
    pop = Population(10, 5, 0, 1)
    print("População Inicial:")
    for ind in pop.indivs:
        print(ind.genome, ind.evaluate_fitness())
    
    best_indiv = pop.best_indiv()
    print("\nMelhor Indivíduo:", best_indiv.genome, best_indiv.evaluate_fitness())

    selected = pop.selection(4)
    print("\nIndivíduos Selecionados:")
    for ind in selected:
        print(ind.genome, ind.evaluate_fitness())

    offspring = pop.recombination(selected, 6)
    print("\nDescendentes:")
    for ind in offspring:
        print(ind.genome, ind.evaluate_fitness())

    pop.reinsertion(offspring)
    print("\nPopulação após reinserção:")
    for ind in pop.indivs:
        print(ind.genome, ind.evaluate_fitness())
