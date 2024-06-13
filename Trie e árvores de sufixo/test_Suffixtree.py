import unittest
from Suffix_tree import SuffixTree

class TestSuffixTree(unittest.TestCase):
    def setUp(self):
        self.suffix_tree = SuffixTree()

    def test_build_suffix_tree(self):
        texto = "PaLaVra"
        self.suffix_tree.build_suffix_tree(texto)
        self.assertTrue(self.suffix_tree.existe("palavra"))
        self.assertTrue(self.suffix_tree.existe("AVRA"))
        self.assertTrue(self.suffix_tree.existe("vra"))
        self.assertTrue(self.suffix_tree.existe("LAVRA"))
        self.assertTrue(self.suffix_tree.existe("Ra"))
        self.assertTrue(self.suffix_tree.existe("a"))
        self.assertFalse(self.suffix_tree.existe("Falso"))

    def test_insere_e_existe(self):
        palavras = ["amor", "amora", "Ama", "amarillo", "palavra"]
        sequencias = ['ACGT', 'ACGTACGtacg', 'ACCTACGTACGTACGTACGT', 'ACGTACGTACGTACGTACGTACGT', 'ACGTACGTACGTACGTACGTACGTACGT']
        for palavra in palavras:
            self.suffix_tree.insere_sufixo(palavra, 0)
        for sequencia in sequencias:
            self.suffix_tree.insere_sufixo(sequencia, 0)
        
        for palavra in palavras:
            self.assertTrue(self.suffix_tree.existe(palavra))
            self.assertFalse(self.suffix_tree.existe(palavra + "x"))
            self.assertTrue(self.suffix_tree.existe(palavra.upper()))
        
        for sequencia in sequencias:
            self.assertTrue(self.suffix_tree.existe(sequencia))

        testes_falsos = ["amo", "amorzinho", 'xxx', 'lala']
        for palavra in testes_falsos:
            self.assertFalse(self.suffix_tree.existe(palavra))

    def test_procura_sufixo(self):
        palavras = ["amor", "amora", "ama", "amarillo",
                    "palavra", 'ACgt', 'ACGTT', 'ACGTACGTACGTACGT']
        for palavra in palavras:
            self.suffix_tree.insere_sufixo(palavra, 0)
        
        sufixos = ['vra', 'llo', 'gT']
        sufixos_falsos = ['ava', 'ro', 'AGGT', 'fa', 'pre']       
        for sufixo in sufixos:
            self.assertIsNotNone(self.suffix_tree.procura_sufixo(sufixo))
        for sufixo in sufixos_falsos:
            self.assertIsNone(self.suffix_tree.procura_sufixo(sufixo))       


    def test_remove_sufixo(self):
        palavras = ["amor", "amora", "ama", "amarillo",
                    "palavra", 'ACgt', 'ACGTT', 'ACGTACGTACGTACGT']
        for palavra in palavras:
            self.suffix_tree.insere_sufixo(palavra, 0)
        
        para_apagar = ["palavra", "ACgt", 'ACGTT']
        for palavra in para_apagar:
            self.assertTrue(self.suffix_tree.existe(palavra))
            self.assertTrue(self.suffix_tree.remove_sufixo(palavra))
            self.assertFalse(self.suffix_tree.existe(palavra))

        nova_lista = ["ama", "amarillo", 'ACGTACGTACGTACGT']
        for palavra in nova_lista:
            self.assertTrue(self.suffix_tree.existe(palavra))

if __name__ == '__main__':
    unittest.main()