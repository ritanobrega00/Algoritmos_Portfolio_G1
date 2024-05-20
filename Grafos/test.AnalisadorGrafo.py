import unittest
from AnalisadorGrafo import AnalisadorGrafo

class TestAnalisadorGrafo(unittest.TestCase):

    def setUp(self):
        self.grafo = {
            1: {2, 3},
            2: {3},
            3: set(),
            4: {1, 2},
            5: {6},
            6: set()
        }
        self.analisador = AnalisadorGrafo(self.grafo)

    def test_predecessores(self):
        self.assertEqual(self.analisador.predecessores(3), [1, 2])
        self.assertEqual(self.analisador.predecessores(1), [4])
        self.assertEqual(self.analisador.predecessores(5), [])

    def test_sucessores(self):
        self.assertEqual(self.analisador.sucessores(1), [2, 3])
        self.assertEqual(self.analisador.sucessores(3), [])
        self.assertEqual(self.analisador.sucessores(5), [6])

    def test_vertices_adjacentes(self):
        self.assertEqual(self.analisador.vertices_adjacentes(1), {2, 3, 4})
        self.assertEqual(self.analisador.vertices_adjacentes(3), {1, 2})
        self.assertEqual(self.analisador.vertices_adjacentes(5), {6})

    def test_grau_entrada(self):
        self.assertEqual(self.analisador.grau_entrada(1), 1)
        self.assertEqual(self.analisador.grau_entrada(3), 2)
        self.assertEqual(self.analisador.grau_entrada(6), 1)

    def test_grau_saida(self):
        self.assertEqual(self.analisador.grau_saida(1), 2)
        self.assertEqual(self.analisador.grau_saida(3), 0)
        self.assertEqual(self.analisador.grau_saida(5), 1)

    def test_grau(self):
        self.assertEqual(self.analisador.grau(1), 3)
        self.assertEqual(self.analisador.grau(3), 2)
        self.assertEqual(self.analisador.grau(5), 1)

    def test_busca_profundidade(self):
        self.assertEqual(self.analisador.busca_profundidade(1), [1, 2, 3])
        self.assertEqual(self.analisador.busca_profundidade(4), [4, 1, 2, 3])
        self.assertEqual(self.analisador.busca_profundidade(5), [5, 6])

    def test_busca_largura(self):
        self.assertEqual(self.analisador.busca_largura(1), [1, 2, 3])
        self.assertEqual(self.analisador.busca_largura(4), [4, 1, 2, 3])
        self.assertEqual(self.analisador.busca_largura(5), [5, 6])

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)