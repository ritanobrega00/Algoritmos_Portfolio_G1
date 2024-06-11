from automato import Automata
import unittest

class TestAutomataATCG(unittest.TestCase):
    def setUp(self):
        self.automato = Automata("ATCG", "ATCG")

    def test_nextState(self):
        self.assertEqual(self.automato.nextState(0, 'A'), 1)
        self.assertEqual(self.automato.nextState(0, 'C'), 0)
        self.assertEqual(self.automato.nextState(2, 'G'), 0)

    def test_applySeq(self):
        seq1 = "ATCGATCGATCG"
        self.assertEqual(self.automato.applySeq(seq1), [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4])
        seq2 = "CGATCG"
        self.assertEqual(self.automato.applySeq(seq2), [0, 0, 1, 2, 3, 4])
        seq3 = "GGAGTATA"
        self.assertEqual(self.automato.applySeq(seq3), [0, 0, 1, 0, 0, 1, 2, 1])

    def test_occurencesPattern(self):
        text1 = "ATCGATCGATCG"
        self.assertEqual(self.automato.occurencesPattern(text1), (3, [0, 4, 8]))
        text2 = "CGATCG"
        self.assertEqual(self.automato.occurencesPattern(text2), (1, [2]))
        text3 = "GGAGTATA"
        self.assertEqual(self.automato.occurencesPattern(text3), (0, []))

class TestAutomataAC(unittest.TestCase):
    def setUp(self):
        self.automato = Automata("AC", "ACA")

    def test_nextState(self):
        self.assertEqual(self.automato.nextState(0, 'A'), 1)
        self.assertEqual(self.automato.nextState(0, 'C'), 0)
        self.assertEqual(self.automato.nextState(1, 'A'), 1)
        self.assertEqual(self.automato.nextState(1, 'C'), 2)
        self.assertEqual(self.automato.nextState(2, 'C'), 0)

    def test_applySeq(self):
        seq1 = "ACACACA"
        self.assertEqual(self.automato.applySeq(seq1), [1, 2, 3, 2, 3, 2, 3])
        seq2 = "CACACACA"
        self.assertEqual(self.automato.applySeq(seq2), [0, 1, 2, 3, 2, 3, 2, 3])
        seq3 = "CACAACAA"
        self.assertEqual(self.automato.applySeq(seq3), [0, 1, 2, 3, 1, 2, 3, 1])

    def test_occurencesPattern(self):
        text1 = "ACACACA"
        self.assertEqual(self.automato.occurencesPattern(text1), (3, [0, 2, 4]))
        text2 = "CACACACA"
        self.assertEqual(self.automato.occurencesPattern(text2), (3, [1, 3, 5]))
        text3 = "CACAACAA"
        self.assertEqual(self.automato.occurencesPattern(text3), (2, [1, 4]))  

if __name__ == '__main__':
    unittest.main()