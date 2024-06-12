import random
from Individual import Individual
from Population import Population

class EvolAlgorithm:
    def __init__(self, tamanho_populacao, comprimento_genoma, limite_inferior, limite_superior, taxa_mutacao, max_geracoes):
        self.tamanho_populacao = tamanho_populacao
        self.comprimento_genoma = comprimento_genoma
        self.limite_inferior = limite_inferior
        self.limite_superior = limite_superior
        self.taxa_mutacao = taxa_mutacao
        self.max_geracoes = max_geracoes
        self.populacao = self.inicializar_populacao()

    def inicializar_populacao(self):
        """
        Inicializa a população com indivíduos aleatórios.
        """
        return [Individual(self.comprimento_genoma, self.limite_inferior, self.limite_superior) for _ in range(self.tamanho_populacao)]

    def avaliar_populacao(self):
        """
        Avalia o fitness de todos os indivíduos da população.
        """
        for individuo in self.populacao:
            self.avaliar(individuo)

    def avaliar(self, individuo):
        """
        Avalia o fitness de um indivíduo específico.
        """
        raise NotImplementedError("Este método deve ser sobrescrito por subclasses")

    def selecionar_pais(self):
        """
        Seleciona pais usando seleção de roleta baseada no fitness.
        """
        fitnesses = [individuo.fitness for individuo in self.populacao]
        total_fitness = sum(fitnesses)
        probabilidades = [fitness / total_fitness for fitness in fitnesses]
        pais = random.choices(self.populacao, probabilidades, k=2)
        return pais

    def crossover(self, pai1, pai2):
        """
        Realiza o crossover entre dois pais para produzir dois filhos.
        """
        ponto_crossover = random.randint(1, self.comprimento_genoma - 1)
        filho1_genoma = pai1.genoma[:ponto_crossover] + pai2.genoma[ponto_crossover:]
        filho2_genoma = pai2.genoma[:ponto_crossover] + pai1.genoma[ponto_crossover:]

        filho1 = Individual(self.comprimento_genoma, self.limite_inferior, self.limite_superior)
        filho1.genoma = filho1_genoma

        filho2 = Individual(self.comprimento_genoma, self.limite_inferior, self.limite_superior)
        filho2.genoma = filho2_genoma

        return filho1, filho2

    def mutacao(self, individuo):
        """
        Realiza a mutação no genoma de um indivíduo com base na taxa de mutação.
        """
        for i in range(len(individuo.genoma)):
            if random.random() < self.taxa_mutacao:
                individuo.genoma[i] = random.uniform(self.limite_inferior, self.limite_superior)

    def substituir_populacao(self, nova_populacao):
        """
        Substitui a população antiga pela nova população.
        """
        self.populacao = nova_populacao

    def executar(self):
        """
        Executa o algoritmo evolutivo por um número máximo de gerações.
        """
        for geracao in range(self.max_geracoes):
            # Avalia o fitness da população atual
            self.avaliar_populacao()

            # Cria uma nova população através de seleção, crossover e mutação
            nova_populacao = []

            while len(nova_populacao) < self.tamanho_populacao:
                # Seleciona pais
                pai1, pai2 = self.selecionar_pais()

                # Realiza o crossover
                filho1, filho2 = self.crossover(pai1, pai2)

                # Realiza a mutação nos filhos
                self.mutacao(filho1)
                self.mutacao(filho2)

                # Avalia o fitness dos filhos
                self.avaliar(filho1)
                self.avaliar(filho2)

                # Adiciona os filhos à nova população
                nova_populacao.append(filho1)
                nova_populacao.append(filho2)

            # Garante que o tamanho da nova população seja igual ao tamanho original
            nova_populacao = nova_populacao[:self.tamanho_populacao]

            # Substitui a população antiga pela nova população
            self.substituir_populacao(nova_populacao)

            # Opcional: Imprime o melhor fitness da geração atual
            melhor_individuo = max(self.populacao, key=lambda indiv: indiv.fitness)
            print(f"Geração {geracao}: Melhor Fitness = {melhor_individuo.fitness}")
