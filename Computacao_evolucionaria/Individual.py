import random

"""Código inspirado no código do professor Miguel Rocha presente no livro Bioinformatic Algorithms"""
class Individual:
    def __init__(self, length: int, lower_bound: float, upper_bound: float):
        self.genome = [random.uniform(lower_bound, upper_bound) for _ in range(length)]
        self.fitness = None

    def evaluate_fitness(self) -> None:
        self.fitness = sum(x**2 for x in self.genome)

class Individuos:
    def __init__(self, size: int, lim_sup: int = 1, lim_inf: int = 0, genome: list = None):
        """
        Inicia um novo objeto da classe individuos.

        Parâmetros:
            size (int): O tamanho do genoma do indivíduo.
            lim_sup (int): O limite superior do genoma do indivíduo.
            lim_inf (int): O limite inferior do genoma do indivíduo.
            genome (list): O genoma do indivíduo. Se não fornecido, será iniciado aleatoriamente.
        """
        self.size = size
        self.lim_sup = lim_sup
        self.lim_inf = lim_inf
        self.genome = genome if genome is not None else self.init_aleat_indiv(size)

    def init_aleat_indiv(self, size: int) -> list:
        """
        Inicia o genoma do indivíduo com valores aleatórios.

        Parâmetros:
            size (int): O tamanho do genoma do indivíduo.

        Retorno:
            list: O genoma iniciado aleatoriamente.
        """
        return [random.randint(self.lim_inf, self.lim_sup) for _ in range(size)]

    def mutation(self) -> None:
        """
        Altera um gene aleatório do genoma do indivíduo.
        """
        pos_gene = random.randint(0, self.size - 1)
        self.genome[pos_gene] = 0 if self.genome[pos_gene] != 0 else 1

    def crossover(self, other: 'Individuos') -> tuple:
        """
        Realiza crossover entre o indivíduo atual (self) e outro indivíduo para gerar dois novos indivíduos.

        Parâmetros:
            Individuos: O outro indivíduo.

        Retorno:
            (Individuos, Individuos): Dois novos indivíduos resultantes do crossover.
        """
        if self.size != other.size:
            raise ValueError("Os indivíduos devem ter tamanhos de genoma iguais para realizar o crossover.")

        crossover_point = random.randint(1, self.size - 1)
        new_genome1 = self.genome[:crossover_point] + other.genome[crossover_point:]
        new_genome2 = other.genome[:crossover_point] + self.genome[crossover_point:]

        return Individuos(size=self.size, genome=new_genome1), Individuos(size=other.size, genome=new_genome2)

    def crossover_multi(self, other: 'Individuos', num_points: int) -> tuple:
        """
        Realiza crossover entre o indivíduo atual (self) e outro indivíduo para gerar dois novos indivíduos.

        Parâmetros:
            Individuos: O outro indivíduo.
            num_points (int): O número de pontos de crossover.

        Retorno:
            (Individuos, Individuos): Dois novos indivíduos resultantes do crossover.
        """
        if self.size != other.size:
            raise ValueError("Os indivíduos devem ter tamanhos de genoma iguais para realizar o crossover.")
        if num_points >= self.size - 1:
            raise ValueError("O número de pontos de crossover deve ser menor que o tamanho do genoma - 1.")

        crossover_points = sorted(random.sample(range(1, self.size), num_points))
        new_genome1, new_genome2 = [], []
        current_parent = self
        for i in range(self.size):
            if i in crossover_points:
                current_parent = other if current_parent is self else self
            new_genome1.append(current_parent.genome[i])
            new_genome2.append(other.genome[i])

        return Individuos(size=self.size, genome=new_genome1), Individuos(size=other.size, genome=new_genome2)

    def get_fitness(self) -> int:
        """
        Retorno:
            int: A aptidão do indivíduo.
        """
        return sum(self.genome)

if __name__ == "__main__":
    # Exemplo de uso
    indiv1 = Individuos(size=10)
    indiv2 = Individuos(size=10)
    print(f"Indivíduo 1: {indiv1.genome}")
    print(f"Indivíduo 2: {indiv2.genome}")
    indiv1.mutation()
    print(f"Indivíduo 1 após mutação: {indiv1.genome}")
    child1, child2 = indiv1.crossover(indiv2)
    print(f"Crossover: {child1.genome}, {child2.genome}")
    print(f"Fitness do indivíduo 1: {indiv1.get_fitness()}")
