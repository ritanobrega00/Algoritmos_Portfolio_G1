import graphviz
import re
import networkx as nx
import matplotlib.pyplot as plt

class RedeMetabolica:
    def __init__(self):
        self.grafo = nx.DiGraph()

    def adicionar_reacao(self, reacao, substratos, produtos, reversivel=False):
        for sub in substratos:
            if sub not in self.grafo:
                self.grafo.add_node(sub)
        for prod in produtos:
            if prod not in self.grafo:
                self.grafo.add_node(prod)
        for sub in substratos:
            self.grafo.add_edge(sub, reacao)
            if reversivel:
                self.grafo.add_edge(reacao, sub)
        for prod in produtos:
            self.grafo.add_edge(reacao, prod)
            if reversivel:
                self.grafo.add_edge(prod, reacao)


    def adicionar_grafo(self, reacao, antes, depois, reversivel=False):
        self.adicionar_reacao(reacao, antes, depois, reversivel)
        self.grafo.add_nodes_from(antes)
        self.grafo.add_nodes_from(depois)

    def parse_reaction_string(self, reaction_string, split_reactions=False):
        reactions = reaction_string.splitlines()
        for reaction in reactions:
            match = re.match(r"\s*(\w+)\s*:\s*(.*?)\s*(=>|<=>)\s*(.*)\s*", reaction)
            if match:
                reacao, antes, tipo, depois = match.groups()
                antes = re.findall(r'\b\w+\b', antes)
                depois = re.findall(r'\b\w+\b', depois)
                reversivel = tipo == "<=>"
                self.adicionar_reacao(reacao, antes, depois, reversivel=reversivel)

    def representar_grafo(self):
        pos = nx.spring_layout(self.grafo)
        nx.draw_networkx_nodes(self.grafo, pos, node_color='g', alpha=0.5)
        nx.draw_networkx_edges(self.grafo, pos, arrows=True)
        nx.draw_networkx_labels(self.grafo, pos)
        plt.show()

rede_metabolica = RedeMetabolica()
rede_metabolica.parse_reaction_string("""
    R1: M1 + M2 => M3 + M4
    R2: M4 + M6 => M3
    R3: M4 + M5 <=> M6
    R4: M2 => M5
""")
rede_metabolica.representar_grafo()
