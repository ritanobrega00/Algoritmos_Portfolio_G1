from random import random, randint, choice, uniform
# Recorremos à parte de definição do objeto feita pelo Prof. Rui Mendes em MotifFinding-incompleto.py

#Funções do Portfolio do semestre passado
def pwm(alignment, pseudo: float = 0):
    bases = 'ATCG'
    pwm_matrix = []
    aligned_seqs = [seq.upper().replace(' ', '') for seq in alignment]

    for pos in zip(*aligned_seqs):
        counts = {base: pos.count(base) + pseudo for base in bases}
        total_count = sum(counts.values())
        pwm_values = [round(counts[base] / total_count, 2) for base in bases]
        pwm_matrix.append(pwm_values)
    return pwm_matrix

def prob_seq(seq, PWM):
    seq = seq.upper().replace(' ', '')
    product = 1.0
    for pos, elem in enumerate(seq):
        product *= PWM[pos][elem_index(elem)]
    return product

def elem_index(elem):
    return {'A': 0, 'T': 1, 'C': 2, 'G': 3}[elem]


class GibsSampling:
    """   
    Algoritmo de Gibs Sampling
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
    
    def readFile(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                self.seqs.append(line.strip().upper())
    
    #Código desenvolvido por nós para o Gibbs Sampling
    def RandomOffsets(self):
        offsets_dict = dict()
        for seq in self.seqs:
            offsets_dict[seq] = randint(0, len(self.seqs[0]) - self.motifSize)
        return offsets_dict
    
    def CreateMotifs(self, offsets:dict):
        lista_motifs = []
        for seq, pos in offsets.items():
            motif = seq[pos: pos + self.motifSize]
            lista_motifs.append(motif)
        return lista_motifs
    
    def Score(self, offsets):
        #adaptada do Prof. Rui Mendes
        score = 1.0
        motifs = self.CreateMotifs(offsets)
        pwm_matrix = pwm(motifs)
        
        for j in range(self.motifSize):
            max_col = max(pwm_matrix[j][i] for i in range(4))
            score *= max_col
        return score   

    def prob_para_pos(self, seq):
        motifs = self.seqs.copy()
        pwm_matriz = pwm(motifs)
        probabilidades = {}
        list_prob = [prob_seq(seq[pos:pos + self.motifSize], pwm_matriz) for pos in range(len(seq) - self.motifSize + 1)]
        total_prob = sum(list_prob)
        for pos, prob in enumerate(list_prob):
            probabilidades[pos] = prob / total_prob
        return probabilidades

    def RandomSelection(self, offsets:dict):
        assert all(len(seq)==len(self.seqs[0]) for seq in self.seqs), 'As sequências não têm o mesmo tamanho'
        sequence_selected = choice(self.seqs)
        offsets.pop(sequence_selected)
        probabilidades = self.prob_para_pos(sequence_selected)
        cutoff = uniform(0, sum(probabilidades.values()))
        return sequence_selected, probabilidades, cutoff

    def Roleta(self, offsets):
        sequence_selected, probabilidades, cutoff = self.RandomSelection(offsets)
        acum = 0.0
        for pos, prob in probabilidades.items():
            acum += prob
            if acum >= cutoff:
                return sequence_selected, pos
        return sequence_selected, list(probabilidades.keys())[0]

    def Gibs(self, max_iter=100, min_improvement=1e-6):
        best_score = -float('inf')
        best_offsets = None
        current_offsets = self.RandomOffsets()
        
        for _ in range(max_iter):
            sequence, pos = self.Roleta(current_offsets)
            current_offsets[sequence] = pos
            score = self.Score(current_offsets)
            
            if score > best_score + min_improvement:
                best_score = score
                best_offsets = current_offsets.copy()
        
        best_motifs = self.CreateMotifs(best_offsets)
        return best_offsets, best_motifs

