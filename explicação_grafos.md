import io -> importa o módulo io, que fornece classes para trabalhar com entrada e saída de dados

from contextlib import redirect_stdout -> função usada para redirecionar a saída padrão para um objeto específico

- class Grafo_orientado: definimos uma classe chamada Grafo_orientado. Esta classe representa um grafo orientado, onde os nós têm arestas unidirecionais entre si.

- def __init__(self): Este é o método construtor da classe. É chamado automaticamente quando um novo objeto da classe é criado. Inicializa o objeto criando um dicionário vazio chamado grafo.

- def adicionar_no(self, v): Este método permite adicionar um novo nó ao grafo. Se o nó já existir no grafo, não acontece nada. Caso contrário, um conjunto vazio é adicionado ao nó, no dicionário grafo.

- def adicionar_aresta(self, u, v): Este método permite adicionar uma aresta direcionada do nó u para o nó v. É usado o método adicionar_no() para garantir que ambos os nós existam no grafo e, em seguida, adiciona v ao conjunto de nós adjacentes a u no dicionário grafo.

- def __repr__(self): Este método é chamado quando a função repr() é chamada no objeto. É retornada uma representação em string do grafo, que neste caso é o dicionário grafo convertido em string.

- def __str__(self): Este método  é chamado quando a função str() é chamada no objeto. É retornada uma representação de string mais legível do grafo. Utiliza um objeto de io.StringIO como armazenamento de memória temporário e redireciona a saída padrão para este usando redirect_stdout(). Em seguida, itera sobre o dicionário grafo e imprime cada nó seguido pela lista de nós adjacentes, separados por "=>". Por fim, retorna o conteúdo que foi armazendo na memória, como uma string.


- predecessores(self, vertice): Este método retorna uma lista dos predecessores do vértice dado. Itera sobre cada vértice no grafo e verifica se o vértice de entrada é um sucessor desse vértice. Se for, adiciona o vértice atual à lista de predecessores.

- sucessores(self, vertice): Este método retorna uma lista dos sucessores do vértice dado. Acede diretamente ao dicionário de adjacência do vértice no grafo para obter a lista de seus sucessores.

- vertices_adjacentes(self, vertice): Este método retorna um conjunto contendo todos os vértices adjacentes ao vértice dado. Faz a união dos conjuntos de predecessores e sucessores do vértice.

- grau_entrada(self, vertice): Este método retorna o grau de entrada do vértice, ou seja, o número de predecessores que o vértice possui. Usa a função len() para contar o número de predecessores.

- grau_saida(self, vertice): Este método retorna o grau de saída do vértice, ou seja, o número de sucessores que o vértice possui. Usa a função len() para contar o número de sucessores.

- grau(self, vertice): Este método retorna o grau do vértice, ou seja, o número total de vértices adjacentes a ele. Usa a função len() para contar o número de vértices adjacentes.

- busca_profundidade(self, vertice_inicial, visitados=None): Este método implementa a busca em profundidade a partir do vértice inicial dado. Usa uma lista 'visitados' para rastrear os vértices visitados durante a busca. O método é recursivo, onde para cada vizinho do vértice atual, chama recursivamente a função de busca profundidade. Retorna a lista de vértices visitados.

- busca_largura(self, vertice_inicial, visitados=None): Este método implementa a busca em largura a partir do vértice inicial dado. Usa a lista 'visitados' para rastrear os vértices visitados durante a busca. Usa a 'fila' para garantir que os vértices sejam visitados na ordem correta. Itera sobre os vértices na fila, visitando cada vértice e adicionando os seus sucessores a esta. Por fim, retorna a lista de vértices visitados.


