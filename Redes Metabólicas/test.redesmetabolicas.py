import unittest
from io import StringIO
from contextlib import redirect_stdout
from Grafo_orientado import Grafo_orientado
from RedeMetabolica import RedeMetabolica

class TestRedeMetabolica(unittest.TestCase):

    def test_adicionar_reacao(self):
        rede = RedeMetabolica()
        rede.adicionar_reacao('R1', ['M1', 'M2'], ['M3'])
        expected_nodes = {'M1', 'M2', 'M3', 'R1'}
        for node in expected_nodes:
            self.assertTrue(rede.grafo.has_node(node))
        expected_edges = {('M1', 'R1'), ('M2', 'R1'), ('R1', 'M3')}
        for edge in expected_edges:
            self.assertTrue(rede.grafo.has_edge(*edge))

    def test_parse_reaction_string(self):
        rede = RedeMetabolica()
        rede.parse_reaction_string("""
            R1: M1 + M2 => M3
            R2: M3 => M4 + M5
        """)
        expected_nodes = {'M1', 'M2', 'M3', 'M4', 'M5', 'R1', 'R2'}
        for node in expected_nodes:
            self.assertTrue(rede.grafo.has_node(node))
        expected_edges = {('M1', 'R1'), ('M2', 'R1'), ('R1', 'M3'), ('M3', 'R2'), ('R2', 'M4'), ('R2', 'M5')}
        for edge in expected_edges:
            self.assertTrue(rede.grafo.has_edge(*edge))

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
