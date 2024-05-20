Os grafos são amplamente utilizados em diversas áreas, incluindo ciência da computação, redes, matemática, e muitas outras, para modelar relações entre entidades.
Um grafo G=(V,E) é uma estrutura matemática composta por:
- Um conjunto V de vértices ou nós
- Um conjunto E de pares de nós, designados por ramos, conexões, ligações ou arcos, cada um ligando dois nós. Estes arcos podem ter
uma orientação (pares ordenados) ou não.


Os grafos podem ser:
- Grafos Orientados (ou Digrafos):
São grafos nos quais as arestas têm uma direção associada a elas. Isto é, significa que a relação entre dois vértices é unidirecional, indo de um vértice de origem para um vértice de destino. 
- Grafos Não Orientados:
São grafos onde as arestas não têm direção associada a elas. Isso significa que a relação entre dois vértices é bidirecional, sem uma distinção entre vértice de origem e vértice de destino.

Num grafo orientado G = (V,E):
– Um vértice s é sucessor do vértice v se existe em E o par ordenado (v,s)
– Um vértice p é antecessor do vértice v se existe em E o par ordenado (p,v)
Se existir em E o par ordenado (p,s), os vértices p e s dizem-se adjacentes (i.e. dois vértices são adjacentes se um é sucessor do outro)

O grau de um nó é definido como o número de ligações que ligam esse nó a outros nós, i.e. é o nº de nós adjacentes.
Se o grafo é orientado, podem definir-se:
• o grau de entrada: número de ligações que chegam a esse nó (nº de predecessores)
• o grau de saída: número de ligações que saem desse nó (nº de sucessores)

Existem duas estratégias que podem ser usadas para definir a ordem de exploração dos nós numa travessia:
– Em largura: começa pelo nó origem, depois explora todos os seus sucessores, depois os sucessores destes, e assim sucessivamente até todos os nós atingíveis terem sido explorados;
– Em profundidade: começa pelo nó origem e explora o 1º sucessor, seguido pelo 1º sucessor deste e assim sucessivamente até não haver mais sucessores e ter que se fazer “backtracking”.


Classe Grafo_orientado: 
definimos uma classe chamada Grafo_orientado. Esta classe representa um grafo orientado, onde os nós têm arestas unidirecionais entre si.

- def __init__(self): Este é o método construtor da classe. É chamado automaticamente quando um novo objeto da classe é criado. Inicializa o objeto criando um dicionário vazio chamado grafo.

- def adicionar_no(self, v): esta função permite adicionar um novo nó ao grafo. Se o nó já existir no grafo, não acontece nada. Caso contrário, um conjunto vazio é adicionado ao nó, no dicionário grafo.

- def adicionar_aresta(self, u, v): Esta função permite adicionar uma aresta direcionada do nó u para o nó v. É usado o método adicionar_no() para garantir que ambos os nós existam no grafo e, em seguida, adiciona v ao conjunto de nós adjacentes a u no dicionário grafo.

- def __repr__(self): Esta função permite que seja retornada uma representação string do objeto grafo, mostrando o seu conteúdo.
  
- def __str__(self): Esta função permite que seja retornada uma representação de string mais legível do grafo. Utiliza um objeto de io.StringIO como armazenamento de memória temporário e redireciona a saída padrão para este usando redirect_stdout(). Em seguida, itera sobre o dicionário grafo e imprime cada nó seguido pela lista de nós adjacentes, separados por "=>". Por fim, retorna o conteúdo que foi armazendo na memória, como uma string.

Classe AnalisadorGrafo:
Esta classe oferece métodos para análise e exploração do grafo, como a determinação de predecessores, sucessores, grau de entrada, grau de saída e buscas em largura e profundidade.

- __init__(self, grafo): O método inicializador recebe um objeto grafo da classe 'Grafo_orientado' como parâmetro e armazena-o para uso posterior;

- predecessores(self, vertice): Esta função retorna uma lista dos predecessores do vértice dado. Itera sobre cada vértice no grafo e verifica se o vértice de entrada é um sucessor desse vértice. Se for, adiciona o vértice atual à lista de predecessores.

- sucessores(self, vertice): Esta função retorna uma lista dos sucessores do vértice dado. Acede diretamente ao dicionário de adjacência do vértice no grafo para obter a lista dos seus sucessores.

- vertices_adjacentes(self, vertice): Esta função retorna um conjunto que contém todos os vértices adjacentes ao vértice dado. Faz a união dos conjuntos de predecessores e sucessores do vértice.

- grau_entrada(self, vertice): Esta função retorna o grau de entrada do vértice, ou seja, o número de predecessores que o vértice possui. Usa a função len() para contar o número de predecessores.

- grau_saida(self, vertice): Esta função retorna o grau de saída do vértice, ou seja, o número de sucessores que o vértice possui. Usa a função len() para contar o número de sucessores.

- grau(self, vertice): Esta função retorna o grau do vértice, ou seja, o número total de vértices adjacentes a ele. Usa a função len() para fazer esta contagem.

- busca_profundidade(self, vertice_inicial, visitados=None): Esta função implementa a busca em profundidade a partir do vértice inicial dado. Usa uma lista 'visitados' para rastrear os vértices visitados durante a busca. O método é recursivo, onde para cada vizinho do vértice atual, chama recursivamente a função de busca profundidade. Retorna a lista de vértices visitados.

- busca_largura(self, vertice_inicial, visitados=None): Esta função implementa a busca em largura a partir do vértice inicial dado. Usa a lista 'visitados' para rastrear os vértices visitados durante a busca. Usa a 'fila' para garantir que os vértices sejam visitados na ordem correta. Itera sobre os vértices na fila, visitando cada vértice e adicionando os seus sucessores a esta. Por fim, retorna a lista de vértices visitados.


