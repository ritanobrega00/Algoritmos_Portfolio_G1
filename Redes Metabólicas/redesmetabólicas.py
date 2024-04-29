import re
import graphviz
from IPython.display import Image, display

class RedeMetabolica(AnalisadorGrafo):
    def __init__(self):
        super().__init__()
        self.grafo = Grafo_orientado()

    def adicionar_reacao(self, reacao, substratos, produtos, reversivel=False):
        for R in substratos:
            self.grafo.adicionar_aresta(R, reacao)
            if reversivel:
                self.grafo.adicionar_aresta(reacao, R)
        for R in produtos:
            self.grafo.adicionar_aresta(reacao, R)
            if reversivel:
                self.grafo.adicionar_aresta(R, reacao)

    def adicionar_grafo(self, reacao, antes, depois, reversivel=False):
        self.adicionar_reacao(reacao, antes, depois, reversivel)
        for M in antes:
            self.grafo.adicionar_no(M)
        for M in depois:
            self.grafo.adicionar_no(M)

    def parse_reaction_string(self, reaction_string, split_reactions=False):
        reactions = reaction_string.splitlines()
        G = graphviz.Digraph()  # Criar um novo objeto Digraph para representar o grafo
        for reaction in reactions:
            match = re.match(r"\s*(\w+)\s*:\s*(.*?)\s*(=>|<=>)\s*(.*)\s*", reaction)
            if match:
                reacao, antes, tipo, depois = match.groups()
                antes = re.split(r'\s*\+\s*', antes)
                depois = re.split(r'\s*\+\s*', depois)
                reversivel = tipo == "<=>"

                self.adicionar_grafo(reacao, antes, depois, reversivel=reversivel)

        G.attr(rankdir='LR')
        for u in self.grafo.grafo:
            if u.startswith('R'):
                G.node(u, shape="square", color="orange", fontcolor="white", style="filled")
            elif u.startswith('M'):
                G.node(u, shape="circle", color="green", fontcolor="white", style="filled")
            for v in self.grafo.grafo[u]:
                if v.startswith('R'):
                    G.node(v, shape="square", color="orange", fontcolor="white", style="filled")
                elif v.startswith('M'):
                    G.node(v, shape="circle", color="green", fontcolor="white", style="filled")
                G.edge(u, v)

        display(G.render('output', format='png'))

# Exemplo de uso:
rede = RedeMetabolica()
reacoes = """
R1: M1 + M2 => M3 + M4
R2: M3 + M5 => M6
R3: M6 + M7 <=> M8 + M9
R4: M4 + M10 => M11
"""
rede.parse_reaction_string(reacoes)

display(Image(filename='output.png'))