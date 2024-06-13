* __init__
Construtor que inicia o objeto SuffixTree, criando uma Trie com raiz (nó original) zero e inicinado a contagem em 1, útil para a numeração dos nós posteriores.

* __str__
Usa a mesma lógica das Tries, usando o pprint para devolver em forma de string um dicionário que representa a árvore

* existe(palavra)
Função que verifica se determinada palavra (inpt, str). Seguindo a mesma lógica implementada na classe Trie, percorre a Trie a partir do nó raiz, seguindo os símbolos da palavra.
Se a palavra for encontrada, retorna True. Caso contrário, retorna False.

* insere_sufixo(sufixo, start_index)
Função que insere determinado sufixo (input, str) na Árvore começando na posição indicada (start_index, int).
Percorre a Trie a partir do nó raiz, criando novos nós conforme necessário. Quando o sufixo é totalmente inserido, marca o nó final com 'None' para indicar o final do sufixo.

* build_suffix_tree(texto)
Função que constrói a árvore a partir de um determinado texto.
Percorre o texto, inserindo cada sufixo (a partir de cada posição inicial) com o insere_sufixo().

* procura_sufixo(sufixo)
Semelhante ao existe, mas retorna o número do nó final se o sufixo for encontrado.

* remove_sufixo(sufixo)
Encontra o nó final do sufixo usando procura_sufixo(), e então remove o sufixo deletando os nós correspondentes ao sufixo.
Se o sufixo não for encontrado, retorna False.
