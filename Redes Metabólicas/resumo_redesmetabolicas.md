As redes metabólicas são representações do metabolismo, que é o conjunto de todas as reações químicas e as substâncias envolvidas nelas. Numa rede metabólica, os componentes individuais, como as reações (ou enzimas) e as substâncias (substratos e produtos das reações), são representados como nós. Existem diversos tipos de redes possíveis:

- Rede de metabolitos: Nesta rede, os nós representam os compostos químicos e as reações são representadas pelas conexões entre esses compostos.
- Rede de reações: Aqui, os nós são as próprias reações e as conexões entre elas são representadas pelos metabólitos compartilhados.
- Rede de metabolitos e reações: Nesta rede, os nós representam tanto os compostos quanto as reações, e as conexões indicam a participação dos compostos nas reações como substratos ou produtos.
  
Uma representação comum para essas redes é através de grafos bipartidos, onde um grafo G=(V,E) é considerado bipartido quando:
O seu conjunto de vértices V pode ser dividido em dois conjuntos V1 e V2, de modo que a união de V1 e V2 é igual a V, e a interseção entre eles é vazia.
O conjunto de arestas E contém apenas pares onde um dos vértices pertence a V1 e o outro a V2, ou seja, só existem conexões entre elementos de diferentes conjuntos, e não há conexões entre elementos do mesmo conjunto.
Portanto, as redes metabólicas reação-metabolito são exemplos de grafos bipartidos, onde V1 representa o conjunto de metabolitos e V2 representa o conjunto de reações.

Este código define uma classe chamada RedeMetabolica que trabalha com reações metabólicas representadas como um grafo direcionado.
Esta classe importa o 'AnalisadorGrafo' presente no script 'Grafos' deste mesmo reportório;

- o ´método __init__(self)´ cria um espaço vazio (um grafo) onde podemos adicionar informações sobre uma rede metabólica, usando a biblioteca NetworkX.

- A função 'adicionar_reacao(self, reacao, substratos, produtos, reversivel=False)' recebe como parâmetros o nome da reação, uma lista de substratos, uma lista de produtos, e um parâmetro opcional reversivel que indica se a reação é reversível ou não (padrão é False). Para cada substrato na lista 'substratos', verifica se ele já está no grafo. Se não estiver, adiciona-o como um nó. E faz exatamente a mesma coisa com os produtos. 
Em seguida, adiciona as arestas representando a reação: uma aresta do substrato para a reação e uma do reação para o produto. Se a reação for reversível, também adiciona as arestas no sentido contrário.

- A função 'adicionar_grafo(self, reacao, antes, depois, reversivel=False)' simplifica a adição de uma reação e dos seus nós adjacentes ao grafo.
Chama a função 'adicionar_reacao' com os parâmetros fornecidos e, em seguida, adiciona os nós de substratos (antes) e produtos (depois) ao grafo.

- A função 'parse_reaction_string(self, reaction_string, split_reactions=False)' analisa uma string contendo informações sobre as reações metabólicas e adiciona-as ao grafo. Recebe uma 'reaction_string' contendo uma lista de reações, onde cada linha representa uma reação. Divide a string em linhas e itera sobre elas.
Usa expressões regulares para extrair informações sobre a reação (nome, substratos, produtos e tipo) de cada linha.

- Por fim, a função 'representar_grafo(self)' representa graficamente o grafo utilizando a biblioteca NetworkX e Matplotlib.
Usa o algoritmo de layout Spring para posicionar os nós do grafo. Desenha os nós, as arestas e os rótulos do grafo atarvés da biblioteca NetworkX.
Exibe o gráfico usando a função plt.show() do Matplotlib.

