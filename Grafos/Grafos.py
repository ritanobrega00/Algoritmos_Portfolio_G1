import io
from contextlib import redirect_stdout

class Grafo_orientado:
    def __init__(self):
        self.grafo = {}

    def adicionar_no(self, v):
        if v not in self.grafo:
            self.grafo[v] = set()

    def adicionar_aresta(self, u, v):
        self.adicionar_no(u)
        self.adicionar_no(v)
        self.grafo[u].add(v)

    def __repr__(self):
        return str(self.grafo)
        
    def __str__(self):
        with io.StringIO() as F, redirect_stdout(F):
            for u in self.grafo:
                print(u, [v for v in self.grafo[u]], sep=" => ")
            return F.getvalue()

# Exemplo de uso
G = Grafo_orientado()
G.adicionar_aresta(1, 2)
G.adicionar_aresta(1, 3)
G.adicionar_aresta(2, 3)
G.adicionar_no('Grupo1')
print(G)


class AnalisadorGrafo:
    def __init__(self, grafo):
        self.grafo = grafo

    def predecessores(self, vertice):
        return [v for v in self.grafo if vertice in self.grafo[v]]

    def sucessores(self, vertice):
        return [v for v in self.grafo[vertice]]

    def vertices_adjacentes(self, vertice):
        return set(self.predecessores(vertice)) | set(self.sucessores(vertice))

    def grau_entrada(self, vertice):
        return len(self.predecessores(vertice))

    def grau_saida(self, vertice):
        return len(self.sucessores(vertice))

    def grau(self, vertice):
        return len(self.vertices_adjacentes(vertice))

    def busca_profundidade(self, vertice_inicial, visitados=None):
        if visitados is None:
            visitados = []

        assert vertice_inicial in self.grafo, f"O grafo não possui o vértice {vertice_inicial}"

        if vertice_inicial not in visitados:
            visitados.append(vertice_inicial)
            for vizinho in self.grafo[vertice_inicial]:
                self.busca_profundidade(vizinho, visitados)

        return visitados

    def busca_largura(self, vertice_inicial, visitados=None):
        if visitados is None:
            visitados = []

        assert vertice_inicial in self.grafo, f"O grafo não possui o vértice {vertice_inicial}"
        fila = [vertice_inicial]

        while fila:
            vertice_atual = fila.pop(0)
            if vertice_atual not in visitados:
                visitados.append(vertice_atual)
                fila.extend(self.sucessores(vertice_atual))

        return visitados
    
#exemplo de uso

import random
import networkx as nx
import matplotlib.pyplot as plt

class Grafo_aleatorio(Grafo_orientado):
    def __init__(self, nos, probabilidade=0.2):
        super().__init__()
        self.grafo_nx = nx.DiGraph()

        for i in range(nos):
            for j in range(nos):
                if i != j and random.random() < probabilidade:
                    self.adicionar_aresta(i, j)
                    self.grafo_nx.add_edge(i, j)

G = Grafo_aleatorio(10)
# Desenhar o grafo
nx.draw(G.grafo_nx, with_labels=True)
plt.show()