A Transformação de Burrows-Wheeler (BWT) é um método de compressão de sequências que visa converter repetições de símbolos em sequências de símbolos repetidos.
O BWT funciona através de rotações cíclicas da sequência original, que são então ordenadas lexicograficamente. 
Isto resulta numa matriz onde a primeira coluna é a ordenação lexicográfica dos caracteres do alfabeto, 
e a última coluna é uma reorganização dos caracteres da sequência original. Essa última coluna é a Transformada de Burrows-Wheeler.

Classe BWT:
 - Método __init__: O construtor da classe BWT inicializa o objeto BWT. Ele recebe uma sequência seq como entrada e um parâmetro opcional sufixarray. Se sufixarray for verdadeiro,também construirá o sufix array.
O BWT é construído chamando o método buildbwt e a primeira coluna do BWT é obtida chamando get_first_col.

- Função buildbwt: constrói a transformação de Burrows-Wheeler da sequência. Ele cria uma lista de todas as rotações cíclicas da sequência, ordena essa lista e, em seguida, extrai o último caractere de cada
string rotacionada para formar o BWT. Se sufixarray for verdadeiro, também constrói o sufix array.

- Função get_first_col: Esta função obtém a primeira coluna do BWT, que é a coluna ordenada alfabeticamente do BWT.

- Função find_occ: retorna uma lista de tuples onde cada tuple é formada por um caractere do BWT e o número de ocorrências desse caractere até aquele ponto no BWT.

  -Função inverse_bwt: realiza a operação inversa da transformação de Burrows-Wheeler. É usada a lista de ocorrências para reconstruir a sequência original.
 
 - Função last_to_first: retorna uma lista que mapeia os índices das últimas colunas do BWT para as primeiras colunas do BWT.
 
 - Função bw_matching: realiza a correspondência de padrões no BWT. É retornada uma lista de índices onde o padrão 'patt' é encontrado no BWT.

 - Função bw_matching_pos: Esta função retorna as posições no texto original onde os padrões correspondentes ao padrão 'patt' são encontrados.
