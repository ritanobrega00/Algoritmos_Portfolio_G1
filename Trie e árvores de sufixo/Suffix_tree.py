import pprint
from collections import defaultdict

class SuffixTree:
    """
    Classe SuffixTree utilizando Trie para armazenar sufixos de palavras.
    """
    def __init__(self):
        self.nos = {0: defaultdict(int)}
        self.num = 1
        self.text = ""

    def __str__(self):
        return pprint.pformat(dict(self.nos))

    def print_tree(self):
        for k, v in self.nos.items():
            if k == 0:
                print(f"Raiz -> {dict(v)}")
            else:
                print(f"Nó {k} -> {dict(v)}")

    def existe(self, sufixo):
        no = 0
        sufixo = sufixo.upper()
        for simbolo in sufixo:
            if simbolo not in self.nos[no]:
                return False
            no = self.nos[no][simbolo]
        return None in self.nos[no]

    def insere_sufixo(self, sufixo, start_index):
        no = 0
        sufixo = sufixo.upper()
        for i in range(start_index, len(sufixo)):
            simbolo = sufixo[i]
            if simbolo not in self.nos[no]:
                self.nos[no][simbolo] = self.num
                self.nos[self.num] = defaultdict(int)
                self.num += 1
            no = self.nos[no][simbolo]
        self.nos[no][None] = start_index

    def build_suffix_tree(self, texto):
        self.text = texto
        for i in range(len(texto)):
            self.insere_sufixo(texto, i)

    def procura_sufixo(self, sufixo):
        no = 0
        sufixo = sufixo.upper()
        return all(simbolo in self.nos[no] for simbolo in sufixo) and None in self.nos[no]

    def remove_sufixo(self, sufixo):
        sufixo = sufixo.upper()
        no_final = self.procura_sufixo(sufixo)
        if no_final is None:
            return False  

        if None in self.nos[no_final]:
            del self.nos[no_final][None]

        no = 0
        for simbolo in sufixo:
            if simbolo in self.nos[no]:
                no = self.nos[no][simbolo]
            else:
                return True 

        while no!= 0 and len(self.nos[no]) == 0:
            parent_no = None
            for no_parent, children in self.nos.items():
                for simbolo, child_no in children.items():
                    if child_no == no:
                        parent_no = no_parent
                        parent_simbolo = simbolo
                        break
                if parent_no is not None:
                    del self.nos[parent_no][parent_simbolo]
                    del self.nos[no]
            no = parent_no
        return True

