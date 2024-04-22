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



#Aplicação:
seq = "ACTAGAGACA"
bwt_instance = BWT(seq)
print(bwt_instance.find_occ())

bwt_instance.find_occ(bwt_instance.primeira_f)
bwt_instance.inverse_bwt()


##### Em desenvolvimento:
# Converter a última na primeira; função -> last_to-first
primeira = bwt_instance.find_occ(bwt_instance.primeira_f)
ultima = bwt_instance.find_occ()
res = []

for x in ultima:
  res.append(primeira.index(x))

print(res)

# porcura do padrões - ainda não funciona como deve (rascunho de que foi pensado)
padrao = "AGA"
topo = 0
fundo = len(ultima) - 1 
lista = []

while padrao:
    for x in ultima[topo:fundo]:
        if x[0] == padrao[-1]:
            lista.append(res[ultima.index(x)])
    if lista:
        topo = min(lista)  
        fundo = max(lista)
        print(lista)
        lista = []
    padrao = padrao[:-1]

resultados = list(range(topo, fundo))
print(resultados)

