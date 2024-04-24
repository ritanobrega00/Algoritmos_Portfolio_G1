class BWT:
  def __init__(self, seq):
    self.bwt = self.buildbwt(seq)
    self.primeira_f = self.get_first_col()

  def buildbwt(self, seq):
    seq_nova = seq + "$"
    seqs = [seq_nova]
    while seq_nova[0] != "$":
      x = seq_nova[1:] + seq_nova[0]
      seq_nova = x
      seqs.append(seq_nova)
    ord = sorted(seqs)
    bwt = "".join(list(zip(*ord))[-1])
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


#Aplicação:
seq = "TAGACAGAGA"
bwt_instance = BWT(seq)
print("O BWT para a sequência apresentada é:", bwt_instance.bwt)
print("A primeira coluna da matriz BWT é:", bwt_instance.primeira_f)
print("A BWT com as ocorrências de cada carcter:", bwt_instance.find_occ())
print("A primeira coluna com as ocorrências de cada caracter:", bwt_instance.find_occ(bwt_instance.primeira_f))
print("A sequência original é:", bwt_instance.inverse_bwt())
print("A organização da BWT em relação primeira coluna:", bwt_instance.last_to_first())
print("O padrão inserido está nas linhas:", bwt_instance.bw_matching("AGA"))
