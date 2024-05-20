from MySeq import MySeq
from MyMotifs import MyMotifs
from random import random, randint, choice
# Recorremos às classes MyMotifs e MySeq implementadas nas aulas de Algoritmos, 
# assim como à parte de definição do objeto feita pelo Prof. Rui Mendes em MotifFinding-incompleto.py

class GibbsSampling:
    """   
    Algoritmo de Gibbs Sampling
    1. Selecionar posições em cada sequência de forma aleatória e formar segmentos respetivos
    2. Escolher aleatóriamente uma sequência
    3. Criar um perfil P (com pseudo-contagens) a partir das posições anteriormente definidas
    4. Para cada posição p na sequência escolhida, calcular a probabilidade do segmento iniciado em p com tamanho L ter sido gerado por P
    5. Escolher a posição p de acordo com as probabilidades calculadas no passo 4 mas de forma estocastica (através de uma roulette wheel dado que a probabilidade de escolher uma certa posição é proporcional ao seu score)
    6. Repetir os passos de 2 a 5 enquanto for possível melhorar ou atingir um determinado critéio de terminação (como o nº ficxo de iterações ou nº de iterações sem melhorias)    
    """
    
    def __init__(self, size = 8, seqs = None):
        self.motifSize = size
        if (seqs != None):
            self.seqs = seqs
        else:
            self.seqs = []
                    
    def __len__ (self):
        return len(self.seqs)
    
    def __getitem__(self, n):
        return self.seqs[n]
    
    def seqSize (self, i):
        return len(self.seqs[i])
    
    def readFile(self, fic, t):
        for s in open(fic, "r"):
            self.seqs.append(MySeq(s.strip().upper(),t))
        self.alphabet = self.seqs[0].alfabeto()
    
    #Código desenvolvido por nós para o Gibbs Sampling
    def RandomOffsets(self):
        """
    Função que gera um determinado nº de nºs aleatórios dentro de um determinado range 
    (que vai depender do tamanho das seqs dadas)
    Output: dicionário com a lista de nº inteiros aleatóriamente escolhidos como valores e 
        como chaves as sequências associadas
        """
        offsets_dict = dict()
        for seq in self.seqs:
            offsets_dict[seq] = randint(0, len(self.seqs[0]) - self.motifSize)
        return offsets_dict
    
    def CreateMotifs(self, offsets:dict):
        """
        Função que gera segmentos (motifs) em cada sequência com base num dicionário com offsets e as sequencias respetivas
        Output: lista com os segmentos de cada sequência gerads aleatoriamente com tamanho L (self.motifSize)
        """
        lista_motifs = []
        for seq, pos in offsets.items():
            lista_motifs.append(seq[pos: pos + self.motifSize])
        return MyMotifs(lista_motifs)
    
    def Score(self, offsets):
        #adaptada do Prof. Rui Mendes
        score = 1.0
        motif = self.CreateMotifs(offsets)
        motif.createPWM(self)
        matrix = motif.pwm
        for j in range(len(matrix[0])):
            maxcol = max( matrix[i][j] for i in range(len(matrix)) )
            score *= maxcol
        return score  

    def prob_para_pos(self, seq):
        """
        Função para determinar a probabilidade para cada posição na sequência escolhida
        """
        pwm = MyMotifs.createPWM(self)
        list_prob = []
        pos = []
        for pos_seq in range(len(seq) - self.motifSize + 1):
            pos.append(pos_seq)
            list_prob.append( pwm.probabSeq(seq[pos_seq : pos_seq + self.motifSize]))
        prob = [p/sum(list_prob) for p in list_prob]
        return pos, prob

    def RandomSelection(self, offsets:dict):
        """
        Função que:
        1. escolhe offsets aleatórios em cada sequência (recorrendo à random_segments)
        2. seleciona aleatoriamente uma sequência (seq1)
        3. Cria o perfil P a partir das posições escolhidas anteriormente
        4. Calcula a probabilidade de um determinado segmento da seq1 ser gerado por P
        5. escolha aleatória de um valor de cutoff que está entre 0 e 1 (soma das probabilidades para a posição p)
        input: dicionário com as sequências e os respetivos offsets (gerados aleatoriamente pelo random_offsets()
        output: lista de posições p na sequência escolhida aleatóriamente, lista de probabilidades para cada p e o valor de cutoff
        """
        assert all(len(seq)==len(self.seqs[0]) for seq in self.seqs), 'As sequências não têm o mesmo tamanho'
        segmentos_seqs = self.CreateMotifs(offsets)
        sequence_selected = choice(self.seqs)
        x = segmentos_seqs.pop(self.seqs.index(sequence_selected))
        pos, prob = self.prob_para_pos(x, self.motifSize, MyMotifs.createPWM(segmentos_seqs) )
        cutoff = random.uniform(0, sum(prob))
        return sequence_selected, pos, prob, cutoff

    def roleta(self, offsets):
        """Escolha eutócastica da posição p de acordo com as probabilidades calculadas com a função random_selection()"""
        sequence_selected, pos_list, prob_list, _ = self.RandomSelection(offsets)
        total_prob = sum(prob_list)
        val = random.uniform(0, total_prob)
        acum = 0.0
        for i, prob in enumerate(prob_list):
            acum += prob
            if acum >= val:
                return sequence_selected, pos_list[i]
        return sequence_selected, pos_list[0]

    def gibbs(self, max_iter=100, min_improvement=1e-6):
        """
        Algoritmo de Gibbs Sampling que irá encontrar o melhor offset para cada sequência da lista fornecida
        Para não fazer um loop infinito, definimos um critério de terminação que é o nº máximo de iterações e a melhoria mínima que queremos obter
        """
        best_score = -float('inf')
        best_offsets = None
        current_offsets = self.RandomOffsets()
        for _ in range(max_iter):
            sequence, pos = self.roleta(current_offsets)
            current_offsets[sequence] = pos
            score = self.Score(current_offsets)
            if score > best_score + min_improvement:
                best_score = score
                best_offsets = current_offsets.copy()
        best_motifs = self.CreateMotifs(best_offsets)
        return best_offsets, best_motifs

