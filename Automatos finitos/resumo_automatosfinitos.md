Os automatos finitos são como 'máquinas' que processam uma sequência de símbolos passo a passo. À medida que vão lendo cada caractere, estes mudam de estado interno. Essas mudanças de estado dependem apenas do estado atual e do último caractere lido. Ao escolher as transições cuidadosamente, podemos determinar se um padrão específico está presente na sequência até o ponto atual da leitura.

Quando construímos um automato a partir de um padrão, ele pode ser usado para procurar eficientemente todas as ocorrências desse padrão numa sequência. Isso é feito percorrendo a sequência apenas uma vez, atualizando o estado do padrão de acordo com as transições definidas para cada caractere. Quando o estado atual do padrão corresponde ao estado final, significa que o padrão foi encontrado na sequência.

Os automatos finitos são especialmente úteis na bioinformática, onde muitas vezes precisamos de procurar o mesmo padrão em várias sequências diferentes, tornando esta abordagem muito eficiente.

Classe Automata:
- __init__(self, alphabet, pattern): O construtor da classe inicializa o automato com um alfabeto e um padrão. O número de estados do automato é definido como o comprimento do padrão mais um. A tabela de transição é inicializada como um dicionário vazio e, em seguida, construída usando a função 'buildTransitionTable';
- buildTransitionTable(self, pattern): Esta função constrói a tabela de transição do automato, itera sobre todos os estados possíveis e todos os símbolos do alfabeto, preenchendo a tabela de transição com o próximo estado para cada par de estado e símbolo. É chamada a função overlap para calcular o próximo estado com base no padrão atual e o símbolo lido;
- nextState(self, current, symbol): Esta função retorna o próximo estado do automato, dado o estado atual e o símbolo lido.
- applySeq(self, seq): Esta função aplica uma sequência de símbolos ao automato, retornando uma lista de estados alcançados.
- occurencesPattern(self, text): Esta função conta o número de ocorrências do padrão no texto e retorna a quantidade de ocorrências e as posições de início de cada ocorrência.

Função overlap:
- Esta função calcula o maior sufixo de s1 que é um prefixo de s2. Isto é, calcula o comprimento da maior sobreposição entre s1 e s2. Isto é essencial para determinar os próximos estados durante a construção do automato. Isto é feito comparando os sufixos de s1 com os prefixos de s2, e retornando o comprimento da maior sobreposição encontrada.
