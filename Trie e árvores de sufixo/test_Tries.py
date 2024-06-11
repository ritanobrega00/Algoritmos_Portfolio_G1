import unittest
from Tries import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_insere_e_existe(self):
        palavras = ["amor", "amora", "Ama", "amarillo", "palavra"]
        sequências = ['ACGT', 'ACGTACGtacg', 'ACCTACGTACGTACGTACGT', 'ACGTACGTACGTACGTACGTACGT', 'ACGTACGTACGTACGTACGTACGTACGT']
        for palavra in palavras:
            self.trie.insere(palavra)
        for sequência in sequências:
            self.trie.insere(sequência)
        for palavra in palavras:
            self.assertTrue(self.trie.existe(palavra))
            self.assertFalse(self.trie.existe(palavra + "x"))
            self.assertTrue(self.trie.existe(palavra.upper()))
        for sequência in sequências:
            self.assertTrue(self.trie.existe(sequência))
        testes_falsos = ["amo", "amorzinho",'agg', 'AGGT']
        for palavra in testes_falsos:
            self.assertFalse(self.trie.existe(palavra))

    def test_procura_prefixo(self):
        """Teste para verificar prefixos na Trie."""
        palavras = ["amor", "amora", "ama", "amarillo",
                 "palavra", 'ACgt', 'ACGTT', 'ACGTACGTACGTACGT']
        for palavra in palavras:
            self.trie.insere(palavra)
        prefixos = ["ACG", "ac", "Am", 'pal']
        prefixos_falsos = ['palavreado', 'diz', 'AGGT', 'fa', 'pre']
        for prefixo in prefixos:
            self.assertTrue(self.trie.procura_prefixo(prefixo))
        for prefixo in prefixos_falsos:
            self.assertFalse(self.trie.procura_prefixo(prefixo))  

    def test_apaga(self):
        palavras = ["amor", "amora", "ama", "amarillo",
                     "palavra", 'ACgt', 'ACGTT', 'ACGTACGTACGTACGT']
        for palavra in palavras:
            self.trie.insere(palavra)
        para_apagar = ["amor", "amora", 'ACGT']
        for palavra in para_apagar:
            self.trie.apaga(palavra)
            self.assertFalse(self.trie.existe(palavra))
        nova_lista = ["ama", "amarillo", "palavra",
                      'ACGTT', 'ACGTACGTACGTACGT']
        for palavras in nova_lista:
            self.assertFalse(self.trie.existe(palavra))

    def test_add_node(self):
        self.trie.add_node(0, 'P')
        self.trie.add_node(1, 'a')
        self.trie.add_node(2, 'L')
        self.trie.add_node(3, 'a')
        self.trie.add_node(4, 'v')
        self.trie.add_node(5, 'R')
        self.trie.add_node(6, 'a')
        self.trie.nodulos[7]['#$#'] = 0 
        self.assertTrue(self.trie.existe("palavra"))
        self.assertTrue(self.trie.existe("PALAVRA"))
        self.assertFalse(self.trie.existe("palavras"))
        self.assertTrue(self.trie.procura_prefixo("pAla"))
        self.assertFalse(self.trie.procura_prefixo("Par"))


if __name__ == '__main__':
    unittest.main()
