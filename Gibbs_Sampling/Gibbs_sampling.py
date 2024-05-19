from MySeq import MySeq
from MyMotifs import MyMotifs
from random import random, randint
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
            self.alphabet = seqs[0].alfabeto()
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
    
    def createMotifFromIndexes(self, s):
        pseqs = []
        for i,ind in enumerate(s):
            pseqs.append( MySeq(self.seqs[i][ind:(ind+self.motifSize)], self.seqs[i].tipo) )
        return MyMotifs(pseqs)

    def scoreMult(self, s):
        score = 1.0
        motif = self.createMotifFromIndexes(s)
        motif.createPWM()
        mat = motif.pwm
        for j in range(len(mat[0])):
            maxcol = mat[0][j]
            for  i in range(1, len(mat)):
                if mat[i][j] > maxcol: 
                    maxcol = mat[i][j]
            score *= maxcol
        return score  

    #Código desenvolvido por nós para o Gibbs Sampling
    def random_offsets(self):
        """
    Função que gera um determinado nº de nºs aleatórios dentro de um determinado range 
    (que vai depender do tamanho das seqs dadas)
    Output: dicionário com a lista de nº inteiros aleatóriamente escolhidos como valores e 
        como chaves as sequências associadas
        """
        fim_range = len(self.seqs[0]) - self.motifSize
        offsets_dict = dict()
        for i in range(0, len(self.seqs)):
            offsets_dict[self.seqs[i]] = randint(0, fim_range)
        return offsets_dict
    
    def random_segments(self):
        """
        Função que gera segmentos aleatórios em cada sequência
        Output: lista com os segmentos de cada sequência gerads aleatoriamente com tamanho L (self.motifSize)
        """
        offsets = self.random_offsets()
        lista_seg = []
        for seq in offsets.keys():
            initial_pos = offsets[seq]
            final_pos = offsets[seq] + self.motifSize
            lista_seg.append(seq[initial_pos : final_pos])
        return lista_seg
    
    def prob_para_pos(self, seq):
        """
        Função para determinar a probabilidade para cada posição na sequência escolhida
        """
        list_prob = []
        pos = []
        for pos_seq in range(0, len(seq) - self.motifSize):
            pos.append(pos_seq)
            list_prob.append( MyMotifs.probabSeq( seq[pos_seq : pos_seq + self.motifSize - 1]) )
        prob = [x/sum(list_prob) for x in list_prob]
        return pos, prob

    def random_selection(self):
        """
        Função que:
        1. escolhe offsets aleatórios em cada sequência (recorrendo à random_segments)
        2. seleciona aleatoriamente uma sequência (seq1)
        3. Cria o perfil P a partir das posições escolhidas anteriormente
        4. Calcula a probabilidade de um determinado segmento da seq1 ser gerado por P
        5. escolha aleatória de um valor de cutoff que está entre 0 e 1 (soma das probabilidades para a posição p)

        output: lista de posições p na sequência escolhida aleatóriamente, lista de probabilidades para cada p e o valor de cutoff
        """
        assert all(len(seq)==len(self.seqs[0]) for seq in self.seqs), 'As sequências não têm o mesmo tamanho'
        segmentos_seqs = self.random_segments(self.seqs, self.motifSize)
        seq1 = random.choice()
        seg1 = segmentos_seqs.pop(self.seqs.index(seq1))
        pos_list, prob_list = self.prob_para_pos(seg1, self.motifSize, MyMotifs.createPWM(segmentos_seqs) )
        #print(pos_list, prob_list)
        cutoff = random.uniform(0, sum(prob_list))
        #print(cutoff)
        return seq1, pos_list, prob_list, cutoff

    def roleta(self):
        """Escolha eutócastica da posição p de acordo com as probabilidades calculadas com a função random_selection()"""
        seq1, pos_list, prob_list, _ = self.random_selection()
        total_prob = sum(prob_list)
        val = random.uniform(0, total_prob)
        acum = 0.0
        for i, prob in enumerate(prob_list):
            acum += prob
            if acum >= val:
                p = pos_list[i]
                return seq1, p
        return seq1, pos_list[0]

    def gibbs(self, max_iter=10, min_improvement=1e-6):
        """
        Algoritmo de Gibbs Sampling que irá encontrar o melhor offset para cada sequência da lista fornecida
        Para não fazer um loop infinito, definimos um critério de terminação que é o nº máximo de iterações e a melhoria mínima que queremos obter
        """
        best_score = -float('inf')
        best_offsets = {}
        for _ in range(max_iter):
            offsets = {}
            for seq in self.seqs:
                _, p = self.roleta(self.seqs, self.motifSize)
                offsets[seq] = p
            motif = self.createMotifFromIndexes(offsets.values())
            score = self.scoreMult(list(offsets.values()))
            if score > best_score + min_improvement:
                best_score = score
                best_offsets = offsets
        return best_offsets

