import graphviz

class Trie:
    """
    Classe Trie com métodos para inserir, apagar, verificar existência e procurar prefixo de palavras
    Com o objetivo de facilitar a procura de padrões
    """
    def __init__(self):
        """
        Construtor que incia o objeto Trie, criando um Trie vazio com uma raiz/nó inicial (representado pelo índice 0)
        self.num é um contador de nós, que é incrementado sempre que um novo nó é adicionado
        """
        self.nodulos = {0: {}}
        self.num = 0
    
    def __str__(self):
        """ devolve a o dicionário dos nódulos em formato de string para facilotar a visualização"""
        from io import StringIO
        import pprint
        sio = StringIO()
        pprint.pprint(self.nodulos, width=1, stream=sio)
        return sio.getvalue()

    def print_trie(self):
        """ Permite vizualizar a Trie (mais precisamente os nós e os seus ramos) mais facilmente"""
        for k, v in self.nodulos.items():
            print(f"{k} -> {v}")

    def add_node(self, origem, simbolo):
        """
        Função que recebe uma origem (int) e um símbolo (str) e adiciona um nó baseado nesse input
        Sendo a origem o nó que dá origem ao novo nó e o símbolo aquilo que liga ao novo nó
        O contador de nós é atualizado
        """
        self.num += 1
        self.nodulos[origem][simbolo] = self.num
        self.nodulos[self.num] = {}

    def existe(self, palavra):
        """
        Função que verifica se uma determinada palavra existe na Trie. 
        Percorre a Trie seguindo os caracteres da palavra até chegar ao '#$#' (o marcador do final de cada palavra)
        Se a palavra existir devolve True, caso contrário devolve False
        """
        no = 0
        for simbolo in palavra:
            if simbolo not in self.nodulos[no]:
                return False
            no = self.nodulos[no][simbolo]
        return '#$#' in self.nodulos[no]

    def procura_prefixo(self, prefixo):
        """
        Função que verifica se um determinado prefixo existe na Trie
        De forma semelhante à função existe(), porém não necessita de chegar ao final da palavra com o marcador '#$#'
        Se existir devolve True, caso contrário devolve False
        """        
        no = 0
        for simbolo in prefixo:
            if simbolo not in self.nodulos[no]:
                return False
            no = self.nodulos[no][simbolo]
        return True

    def insere(self, palavra):
        """
        Função que adiciona determinada palavra na Trie. 
        Se a palavra já existir, não faz nada. 
        Todavia, se a palavra não existir, adiciona-a, criando um nó para cada caracter da palavra e marca o fim da palavra com '#$#'
        """
        no = 0
        for simbolo in palavra:
            if simbolo not in self.nodulos[no]:
                self.add_node(no, simbolo)
            no = self.nodulos[no][simbolo]
        self.nodulos[no]['#$#'] = 0

    def apaga(self, palavra):
        """
        Função que apaga uma determinada palavra da Trie.
        Primeiro verifica se a palavra existe através da função existe(), se não existir devolve False.
        Se existir, apaga os nós à medida que os percorre começando pelo marcado '#$#' 
        """
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

    #Codifo para visualizar a Trie cedido pelo Prof. Rui Mendes
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






    


