class BWT:
  def __init__(self, seq, sufixarray = False):
    self.bwt = self.buildbwt(seq, sufixarray)
    self.primeira_f = self.get_first_col()

  def buildbwt(self, seq, sufixarray = False):
    seq_nova = seq + "$"
    seqs = [seq_nova]
    while seq_nova[0] != "$":
      x = seq_nova[1:] + seq_nova[0]
      seq_nova = x
      seqs.append(seq_nova)
    ord = sorted(seqs)
    bwt = "".join(list(zip(*ord))[-1])

    if sufixarray:
      sufix = {}
      for i in range(len(seq + "$")):
        sufix[seq[i:]] = i
      self.sa = []
      for s in sorted(sufix):
        self.sa.append(sufix[s])

    return bwt

  def get_first_col(self):
    primeira = []
    for l in self.bwt:
      primeira.append(l)
    Primeira_f = sorted(primeira)
    Primeira_f = "".join([x for x in Primeira_f])
    return Primeira_f

  def find_occ(self, lista=None):
    if lista is None:
      lista = self.bwt
    l = []
    resultado = []
    for t in lista:
      l.append(t)
      resultado.append("{}{}".format(t, l.count(t)))
    return resultado

  def inverse_bwt(self):
    listab = self.find_occ()
    lista = self.find_occ(self.primeira_f)
    elemento = ""
    seq = ""
    for t in listab:
      if t == "$1":
        x = listab.index(t)
        elemento = lista[x]
        seq += elemento[0]
    while len(seq) <= len(listab):
      x = listab.index(elemento)
      elemento = lista[x]
      seq += elemento[0]
      if elemento == "$1":
        break
    return seq

  def last_to_first(self):
    primeira = self.find_occ(self.primeira_f)
    ultima = self.find_occ()
    res = []
    for x in ultima:
      res.append(primeira.index(x))
    return res

  def bw_matching(self, patt):
    ultima = self.find_occ()
    last_to_first = self.last_to_first()
    padrao = patt
    topo = 0
    fundo = len(ultima)-1
    linhas = []
    linhas_padrao = []
    while padrao:
      for x in ultima[topo:fundo+1]:
        if x[0] == padrao[-1]:
          linhas.append(last_to_first[ultima.index(x)])
          if len(linhas) != 0:
            linhas_padrao = linhas
      if linhas:
        topo = min(linhas_padrao)
        fundo = max(linhas_padrao)
        linhas = []
      padrao = padrao[:-1]
    return linhas_padrao
  def bw_matching_pos(self, patt):
    res = []
    for ind_pat in self.bw_matching(patt):
      res.append(self.sa[ind_pat])
    return sorted(res)
