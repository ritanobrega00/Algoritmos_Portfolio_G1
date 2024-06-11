#import graphviz
from io import StringIO
import pprint

class Trie:
    """
    Classe Trie com métodos para inserir, apagar, verificar existência e procurar prefixo de palavras
    Com o objetivo de facilitar a procura de padrões
    """
    def __init__(self):

        self.nodulos = {0: {}}
        self.num = 0
    
    def __str__(self):
        sio = StringIO()
        sio.write(pprint.pformat(self.nodulos, width=1))
        return sio.getvalue()

    def print_trie(self):
        for k, v in self.nodulos.items():
            print(f"{k} -> {v}")

    def add_node(self, origem, simbolo):
        simbolo = simbolo.upper()
        self.num += 1
        self.nodulos[origem][simbolo] = self.num
        self.nodulos[self.num] = {}

    def existe(self, palavra):
        no = 0
        palavra = palavra.upper()
        for simbolo in palavra:
            if simbolo not in self.nodulos[no]:
                return False
            no = self.nodulos[no][simbolo]
        return '#$#' in self.nodulos[no]

    def procura_prefixo(self, prefixo):      
        no = 0
        prefixo = prefixo.upper()
        for simbolo in prefixo:
            if simbolo not in self.nodulos[no]:
                return False
            no = self.nodulos[no][simbolo]
        return True

    def insere(self, palavra):
        no = 0
        palavra = palavra.upper()
        for simbolo in palavra:
            if simbolo not in self.nodulos[no]:
                self.add_node(no, simbolo)
            no = self.nodulos[no][simbolo]
        self.nodulos[no]['#$#'] = 0

    def apaga(self, palavra):
        palavra = palavra.upper()
        if not self.existe(palavra):
            return False
        
        no = 0
        stack = []
        for simbolo in palavra:
            stack.append((no, simbolo))
            no = self.nodulos[no][simbolo]
        stack.append((no, '#$#'))

        for no, simbolo in reversed(stack):
            del self.nodulos[no][simbolo]
            if self.nodulos[no]:
                break
            del self.nodulos[no]

        return True

    #Código para visualizar a Trie cedido pelo Prof. Rui Mendes
    def to_graphviz(self, G=None, t=None, name=None):
        G = G or graphviz.Digraph()
        G.node_attr['shape'] = 'circle'
        G.node_attr['label'] = ' '
        G.node_attr['style'] = 'filled'
        t = t or self.nodulos
        name = name or 'root'
        
        def add_edges(no, name):
            for simbolo, proximo in self.nodulos[no].items():
                simbolo_label = simbolo if simbolo.isalpha() else '$'
                new_name = f"{name}_{simbolo_label}"
                G.edge(name, new_name, label=simbolo_label)
                if simbolo != '#$#':  # continue recursively if not a terminal symbol
                    add_edges(proximo, new_name)
        
        add_edges(0, name)
        return G






    


