Classe True: implementa uma Trie, estrutura de dados que armazena e permite a procura de palavras ou prefixos. Através de determinadas funções, é possível inserir, remover e procurar/verficar a existência de prefixos e palavras completas em cada Trie.

Para visualização da estrutura da Trie é importado e usado o graphviz.

*  __init__()
Construtor que inicia o objeto Trie, criando um Trie vazio com uma raiz/nó inicial (representado pelo índice 0). O atributo 'self.num' é um contador de nós, que é incrementado sempre que um novo nó é adicionado.

*  __str__()
Devolve o dicionário dos nós (a Trie) em formato de string, o que facilita a visualização da Trie.

* print_trie()
Permite imprimir a estrutura da Trie, com os nós e os ramos.

* add_node(self, origem, simbolo)
Função que recebe uma origem (int) e um símbolo (string) e adiciona um nó baseado nesse input.
A origem é o nó atual (aquele que dará origem ao novo nó) e o símbolo é a ligação ao novo nó.

* existe(self, palavra):
Função que verifica se uma determinada palavra (completa) existe na Trie.
Percorre a Trie, começando no nó raiz ('no = 0'), seguindo os caracteres da palavra até chegar ao '#$#' (o marcador do final de cada palavra). Se a palavra existir devolve True, caso contrário devolve False.

* procura_prefixo(self, prefixo)
Função que verifica se um determinado prefixo (input, string) existe na Trie.
Funciona de forma semelhante à função existe(), porém não necessita de chegar ao final da palavra com o marcador '#$#'. Se ao percorrer os caracteres, os encontrar a todos devolve True, caso contrário devolve False.

* insere(self, palavra)
Função que adiciona determinada palavra (input, string) na Trie. 
Percorre a Trie, começando no nó raiz, se determinado símbolo não existir no nó atual, chama a função 'add_node()' para adicionar um novo nó, adicionando a palavra à Trie. Se a palavra já existir, não faz nada. 

* apaga(self, palavra)
Função que apaga/remove uma palavra (input, string) da Trie.
Primeiro verifica se a palavra existe através da função existe(), se não existir devolve False.
Se existir, apaga os nós à medida que os percorre começando pelo marcado '#$#' e indo eliminando os símbolos 'de trás para a frente' da palavra. Se um determinado prefixo tiver outras palavras associadas, a remoção é interrompida. 

    
* to_graphviz(self, G=None, t=None, name=None)
Função para visualizar a Trie cedido pelo Prof. Rui Mendes.
