import unittest
from io import StringIO
from contextlib import redirect_stdout
from Grafo_orientado import Grafo_orientado

class TestGrafoOrientado(unittest.TestCase):

    def test_adicionar_no(self):
        G = Grafo_orientado()
        G.adicionar_no(1)
        G.adicionar_no(2)
        G.adicionar_no(1) 
        self.assertEqual(G.grafo, {1: set(), 2: set()})

    def test_adicionar_aresta(self):
        G = Grafo_orientado()
        G.adicionar_aresta(1, 2)
        G.adicionar_aresta(1, 3)
        G.adicionar_aresta(2, 3)
        self.assertEqual(G.grafo, {1: {2, 3}, 2: {3}, 3: set()})

    def test_str(self):
        G = Grafo_orientado()
        G.adicionar_aresta(1, 2)
        G.adicionar_aresta(1, 3)
        G.adicionar_aresta(2, 3)
        G.adicionar_no('Grupo1')
        expected_output = "1 => [2, 3]\n2 => [3]\n3 => []\nGrupo1 => []\n"
        self.assertEqual(str(G), expected_output)

    def test_repr(self):
        G = Grafo_orientado()
        G.adicionar_aresta(1, 2)
        G.adicionar_aresta(1, 3)
        G.adicionar_aresta(2, 3)
        self.assertEqual(repr(G), "{1: {2, 3}, 2: {3}, 3: set()}")

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
