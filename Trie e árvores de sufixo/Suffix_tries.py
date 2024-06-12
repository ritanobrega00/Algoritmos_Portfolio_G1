import graphviz
from io import StringIO
import pprint

class SuffixTrie:
    """
    Classe SuffixTrie com métodos para inserir, apagar, verificar existência e procurar prefixo de sufixos
    """
    def __init__(self):
        """Inicia a SuffixTrie com um nó inicial e um dicionário vazio."""
        self.nodes = {0: {}}
        self.num = 0
    
    def __str__(self):
        """Retorna a estrutura da SuffixTrie como uma string formatada."""
        sio = StringIO()
        sio.write(pprint.pformat(self.nodes, width=1))
        return sio.getvalue()

    def print_suffix_trie(self):
        """Imprime a estrutura da SuffixTrie, exibindo nós e suas conexões."""
        for k, v in self.nodes.items():
            print(f"{k} -> {v}")

    def add_node(self, origin, symbol):
        """Adiciona um novo nó à SuffixTrie com base no nó de origem e no símbolo."""
        symbol = symbol.upper() 
        self.num += 1 
        self.nodes[origin][symbol] = self.num  
        self.nodes[self.num] = {}  

    def exists(self, suffix):
        """Verifica se um sufixo completo existe na SuffixTrie."""
        node = 0
        suffix = suffix.upper()  
        for symbol in suffix:
            if symbol not in self.nodes[node]:
                return False  
            node = self.nodes[node][symbol]  
        return '#$#' in self.nodes[node]  

    def find_prefix(self, prefix):      
        """Verifica se um prefixo existe como sufixo na SuffixTrie."""
        node = 0  
        prefix = prefix.upper() 
        for symbol in prefix:
            if symbol not in self.nodes[node]:
                return False  
            node = self.nodes[node][symbol]  
        return True 

    def insert_suffix(self, word):
        """Insere todos os sufixos de uma palavra na SuffixTrie."""
        for i in range(len(word)):
            self.insert(word[i:])

    def insert(self, suffix):
        """Insere um único sufixo na SuffixTrie."""
        node = 0  
        suffix = suffix.upper()  
        for symbol in suffix:
            if symbol not in self.nodes[node]:
                self.add_node(node, symbol) 
            node = self.nodes[node][symbol] 
        self.nodes[node]['#$#'] = 0  

    def delete_suffix(self, word):
        """Apaga todos os sufixos de uma palavra da SuffixTrie."""
        for i in range(len(word)):
            self.delete(word[i:])

    def delete(self, suffix):
        """Apaga um único sufixo da SuffixTrie."""
        suffix = suffix.upper() 
        if not self.exists(suffix):
            return False
        
        node = 0 
        stack = [] 
        for symbol in suffix:
            stack.append((node, symbol))  
            node = self.nodes[node][symbol]  
        stack.append((node, '#$#'))  

        for node, symbol in reversed(stack):
            del self.nodes[node][symbol]
            if self.nodes[node]:
                break
            del self.nodes[node]  

        return True

    def to_graphviz(self, G=None, t=None, name=None):
        """Visualiza a estrutura da SuffixTrie usando Graphviz."""
        G = G or graphviz.Digraph()
        G.node_attr['shape'] = 'circle'
        G.node_attr['label'] = ' '
        G.node_attr['style'] = 'filled'
        t = t or self.nodes
        name = name or 'root'
        
        def add_edges(current_node, parent_name):
            """Recursively add edges to the Graphviz object."""
            for symbol, next_node in t[current_node].items():
                symbol_label = symbol if symbol.isalpha() else '$'
                new_name = f"{parent_name}_{symbol_label}"
                G.node(new_name, label=symbol_label)
                G.edge(parent_name, new_name, label=symbol_label)
                add_edges(next_node, new_name)
        
        add_edges(0, name)
        return G
