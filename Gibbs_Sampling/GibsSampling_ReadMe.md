** Algoritmo de Gibs Sampling **
1. Selecionar posições em cada sequência de forma aleatória e formar segmentos respetivos
2. Escolher aleatóriamente uma sequência
3. Criar um perfil P (com pseudo-contagens) a partir das posições anteriormente definidas
4. Para cada posição p na sequência escolhida, calcular a probabilidade do segmento iniciado em p com tamanho L ter sido gerado por P
5. Escolher a posição p de acordo com as probabilidades calculadas no passo 4 mas de forma estocastica (através de uma roulette wheel dado que a probabilidade de escolher uma certa posição é proporcional ao seu score)
6. Repetir os passos de 2 a 5 enquanto for possível melhorar ou atingir um determinado critéio de terminação (como o nº ficxo de iterações ou nº de iterações sem melhorias)    


Para a construção desta classe GibsSampling, recorremos às funções pwm() e prob_seq() implementadas nas aulas de Algoritmos do 1º semestre, assim como à parte de definição do objeto feita pelo Prof. Rui Mendes em MotifFinding-incompleto.py
* __init__(self, size = 8, seqs = None)
Construtor que recebe o tamanho do motif a ser encontrado ('size') definido como 8 caso não seja dado como input e uma lista de sequências onde esse motif será procurado.

* __len__(self)
Retorna o número de sequências.

* __getitem__(self, n)
Retorna a sequência na posição n.

* seqSize(self, i)
Retorna o tamanho da sequência i.

* readFile(self, fic, t)
Lê um arquivo de sequências e as armazena na lista self.seqs, assegurando que não há espaços e todas as letras são maiúsculas.

* RandomOffsets(self)
Função que gera offsets aleatórios para cada sequência.
Através do uso do módulo 'random' , é escolhido dentro de um determinado range (que vai depender do tamanho das sequências dadas) um nº aleatório para cada sequência.
A função devolve um dicionário, onde as chaves são as sequências e os valores os nº inteiros aleatóriamente escolhidos. 

* CreateMotifs(self, offsets)
Função que cria segmentos de cada sequência cuja posição inicial é o offset fornecido à função na forma de dicionário.
Estes segmentos criados seráo os nossos possíveis motifs.
A função devolve uma lista que tem os motifs gerados em cada sequência.

* Score(self, offsets)
Adaptada do Prof. Rui Mendes.
Função que calcula o score dos motifs criados a partir dos offsets fornecidos em forma de dicionário usando as funções CreateMotifs() e pwm().

* prob_para_pos(self, seq)
Função que calcula a probabilidade de cada posição da sequência dada como input (str) gerar um segmento de comprimento self.motifSize.
Recorrendo à função pwm(), é gerada a PWM. É criado um dicionário vazio para armazenar a posição e a probabilidade correspondente.
A probabilidade de determinada posição gerar um segmento de comprimento self.motifSize é calculada recorrendo á função prob_seq.
A função devolve um dicionário onde as chaves são as posições na sequência fornecida e o valor associado é a probabilidade calculada.

* RandomSelection(self, offsets)
Função que recebe um dicionário com as sequências e os respetivos offsets (gerados aleatoriamente pela RandomOffsets()):
  1. Assegura-se que as sequências têm todas o mesmo tamanho
  2. Escolhe offsets aleatórios em cada sequência (recorrendo à CreateMotifs())
  3. Seleciona aleatoriamente uma sequência (seq1)
  4. Cria o perfil P a partir das posições escolhidas anteriormente
  5. Calcula a probabilidade de um determinado segmento da seq1 ser gerado por P
  6. Escolhe aleatóriamente um valor de cutoff que está entre 0 e 1 (correspondente à soma das probabilidades para a posição p)
A função devolve a sequência escolhida aleatoriamente, um dicionário com as posições p nessa sequência e a respetiva probabilidades, e o valor de cutoff.

* roleta(self, offsets):
Função que recebe o dicionário com os offstes para cada sequência e faz a escolha eutócastica da posição p de acordo com as probabilidades calculadas com a função RandomSelection()
A função vai somando as probabilidades correspondentes a cada posição até a soma ultrapassar o valor do cutoff fornecido pela RandomSelection().
Se a soma das probabilidades for maior que o cutoof a função devolve a sequência selecionada aleatoriamente e a posição onde a soma ultrapassou o cutoff.
Se o cutoff nunca for ultrapassado, então a função devolve a sequencias e a primeira posição desta.

 * Gibs(self, max_iter=100, min_improvement=1e-6)
Algoritmo de Gibs Sampling que irá encontrar o melhor offset para cada sequência da lista fornecida.
Para não fazer um loop infinito, definimos um critério de terminação que é o nº máximo de iterações e a melhoria mínima que queremos obter.
A função vai devolver os melhores offsets encontrados e os melhores motifs de acordo com estes critérios.

