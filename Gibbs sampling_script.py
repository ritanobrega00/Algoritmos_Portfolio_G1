#do semestre passado
def pwm(alinhamento, pseudo = 0):
  bases = 'ATCG'
  lista = []

  for seq in alinhamento:
    for p, b in enumerate(seq):
      assert b in bases, f"Caractére {b} na posição {p} da sequência {seq} inválida!"

  for pos in list(zip(*alinhamento)):
    dicionario = {}
    for b in bases:
      dicionario[b] = round((pos.count(b) + pseudo) / (len(alinhamento) + len(bases)*pseudo), 2)

    lista.append(dicionario)
  return lista

import math
def pssm(alinhamento, pseudo = 1):
  bases = 'ATCG'
  lista = []

  for pos in list(zip(*alinhamento)):
    dicionario = {}
    for b in bases:
      dicionario[b] = math.log2((pos.count(b) + pseudo) / (len(alinhamento) + len(bases)*pseudo)) / 0.25

    lista.append(dicionario)
  return lista

def prob_seq(seq, PWM):
  produto = 1
  for pos, elem in enumerate(seq):
    produto *= PWM[pos][elem]
  return produto

def consenso(s1: str, s2: str) -> str:
  nm = 0
  seqf = ""
  nmis = 0
  lim = len(s1)/2

  for x in list(range(len(s1))):
    if s1[x] == s2[x]:
      nm += 1
      seqf += s1[x]
    else:
      nmis += 1
      if nmis <= lim:
        seqf += "N"
  con = [seqf, nm]
  return con


# Funções feitas por Gibbs Sampling
import random
def random_offsets(l_seqs:list, L:int) -> dict:
    """
    Função que gera um determinado nº de nºs aleatórios dentro de um determinado range 
    (que vai depender do tamanho das seqs dadas)
    Input: 
    - l_seqs -> lista de sequências (quantidade de nº para gerar vai ser igual ao nº de seqs da lista)
    - L -> o tamanho do motif (o limite do intervalo que será igual ao tamanho da seq menos o tamanho do motif mais 1)

    Output:
    - dicionário com a lista de nº inteiros aleatóriamente escolhidos como valores e como chaves as sequências associadas
    """
    fim_range = len(l_seqs[0]) - L
    offsets_dict = dict()
    for i in range(0, len(l_seqs)):
        offsets_dict[l_seqs[i]] = random.randint(0, fim_range)
    return offsets_dict

def random_segments(l_seqs, L):
    """
    A partir dos offsets gerados aleatoriamente pela função random_offsets gera os segmentos aleatórios em cada seq
    Input: 
    - l_seqs -> lista de sequências 
    - L -> o tamanho do motif/segmento 

    Output:
    - lista com os segmentos de cada sequência gerads aleatoriamente com tamanho L
    """
    offsets = random_offsets(l_seqs, L)
    lista_seg = []
    for seq in offsets.keys():
        initial_pos = offsets[seq]
        final_pos = offsets[seq] + L
        lista_seg.append(seq[initial_pos : final_pos])
    return lista_seg

def prob_para_pos(seq : str, L:int, matriz_pwm : list[float])-> tuple[list[int], list[float]]:
    list_prob = []
    pos = []
    for pos_seq in range(0, len(seq) - L):
        pos.append(pos_seq)
        list_prob.append( prob_seq( seq[pos_seq : pos_seq + L - 1], matriz_pwm) )
    prob = [x/sum(list_prob) for x in list_prob]
    return pos, prob

def random_selection(l_seqs : list[str] , L : int) -> tuple[list[int], int]:
    """Função que:
    1. escolhe offsets aleatórios em cada sequência (recorrendo à random_segments)
    2. seleciona aleatoriamente uma sequência (seq1)
    3. Cria o perfil P a partir das posições escolhidas anteriormente
    4. Calcula a probabilidade de um determinado segmento da seq1 ser gerado por P
    5. escolha aleatória de um valor de cutoff que está entre 0 e 1 (soma das probabilidades para a posição p)

    output: lista de posições p na sequência escolhida aleatóriamente, lista de probabilidades para cada p e o valor de cutoff
    """
    assert all(len(seq)==len(l_seqs[0]) for seq in l_seqs), 'As sequências não têm o mesmo tamanho'
    segmentos_seqs = random_segments(l_seqs, L)
    seq1 = random.choice(l_seqs)
    seg1 = segmentos_seqs.pop(l_seqs.index(seq1))
    pos_list, prob_list = prob_para_pos(seg1, L, pwm(segmentos_seqs, 1) )
    #print(pos_list, prob_list)
    cutoff = random.uniform(0, sum(prob_list))
    #print(cutoff)
    return seq1, pos_list, prob_list, cutoff
    
def roleta(l_seqs : list[str], L : int) -> int:
    """Escolha eutócastica da posição p de acordo com as probabilidades calculadas com a função random_selection()"""
    max_tentativas = 10
    tentativas = 0
    while p is None and tentativas < max_tentativas:
        seq1, pos_list, prob_list, cutoff = random_selection(l_seqs, L)
        for prob in prob_list:
            if prob >= cutoff:
                #print(prob_list.index(prob))
                p = pos_list[ prob_list.index(prob)]
                return seq1, p
        tentativas += 1

def gibbs_sampling(l_seqs : list[str], L : int) -> dict:
    """Algoritmo de Gibbs Sampling que irá encontrar o melhor offset para cada sequência da lista fornecida"""
    nova_lista = l_seqs[::]
    dicionario = {}
    while len(nova_lista) > 2:
        (seq1, p) = roleta(nova_lista, L)
        dicionario[nova_lista.index(seq1)] = p
        nova_lista.pop(nova_lista.index(seq1))
    return dicionario   
# not working :(  demora muito # não sei se está bem feito