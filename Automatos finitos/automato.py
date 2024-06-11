
class Automata:

    def __init__(self, alphabet, pattern):
        ## Estrutura imposta pelo professor
        self.numstates = len(pattern) + 1
        self.alphabet = alphabet
        self.transitionTable = {}
        self.buildTransitionTable(pattern)

    def buildTransitionTable(self, pattern):
        for q in range(self.numstates):
            for a in self.alphabet:
                if q == 0 and a == pattern[q]:
                    self.transitionTable[(q, a)] = 1
                else:
                    sub_pat =  pattern[:q] + a
                    state = overlap(sub_pat, pattern)
                    self.transitionTable[(q, a)] = state

    def printAutomata(self):
        ## Estrutura imposta pelo professor
        print ("States: " , self.numstates)
        print ("Alphabet: " , self.alphabet)
        print ("Transition table:")
        for k in self.transitionTable.keys():
            print (k[0], ",", k[1], " -> ", self.transitionTable[k])

    def nextState(self, current, symbol):
        res = self.transitionTable[(current, symbol)]
        return res

    def applySeq(self, seq):
        est_atual = 0
        res =[]
        for a in seq:
          q = self.nextState(est_atual, a)
          res.append(q)
          est_atual = q
        return res

    def occurencesPattern(self, text):
        x = self.applySeq(text)
        last = self.numstates - 1
        contador = 0
        ind_f = []
        for i,q in enumerate(x):
          if q == last:
            contador +=1
            ind = i
            ind_f.append(ind - (last -1))
        return contador, ind_f

def overlap(s1, s2):
    ## Função fornecida pelo professor
    maxov = min(len(s1), len(s2))
    for i in range(maxov,0,-1):
        if s1[-i:] == s2[:i]: return i
    return 0
