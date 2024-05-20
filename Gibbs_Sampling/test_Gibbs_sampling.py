import unittest
from MySeq import MySeq
from MyMotifs import MyMotifs
from Gibbs_sampling import GibbsSampling

class TestGibbsSampling(unittest.TestCase):

    def test_RandomOffsets(self):
        seqs = [MySeq("GTAAACAATATTTATAGC", "dna"), MySeq("AAAATTTACCTCGCAAGG", "dna"), 
                MySeq("CCGTACTGTCAAGCGTGG", "dna"), MySeq("TGAGTAAACGACGTCCCA", "dna"), 
                MySeq("TACTTAACACCCTGTCAA", "dna")]
        teste1 = GibbsSampling(8, seqs)
        teste2 = GibbsSampling(2, seqs)
        res1 = {"GTAAACAATATTTATAGC": 7, "AAAATTTACCTCGCAAGG": 11, "CCGTACTGTCAAGCGTGG": 9,
                 "TGAGTAAACGACGTCCCA": 4, "TACTTAACACCCTGTCAA": 1}
        res2 = {"GTAAACAATATTTATAGC": 0, "AAAATTTACCTCGCAAGG": 17, "CCGTACTGTCAAGCGTGG": 9,
                 "TGAGTAAACGACGTCCCA": 9, "TACTTAACACCCTGTCAA": 11}

        self.assertEqual(len(teste1.RandomOffsets()), 5)
        self.assertEqual(len(list(teste2.RandomOffsets())[0]), 18)


    def test_CreateMotifs(self):
        seqs = [MySeq("GTAAACAATATTTATAGC", "dna"), MySeq("AAAATTTACCTCGCAAGG", "dna"), 
                MySeq("CCGTACTGTCAAGCGTGG", "dna"), MySeq("TGAGTAAACGACGTCCCA", "dna"), 
                MySeq("TACTTAACACCCTGTCAA", "dna")]
        teste1 = GibbsSampling(8, seqs)
        offset1 = {"GTAAACAATATTTATAGC": 7, "AAAATTTACCTCGCAAGG": 11, "CCGTACTGTCAAGCGTGG": 9,
                 "TGAGTAAACGACGTCCCA": 4, "TACTTAACACCCTGTCAA": 1}
        self.assertEqual(len(teste1.CreateMotifs(offset1)), 5)
        self.assertEqual(len(teste1.CreateMotifs(offset1)[0]), 8)
        self.assertEqual(teste1.CreateMotifs(offset1), ["AATATTTA", "TTAGAAGG", "TCAAGCGT", "GTAAACGA", "TACTTAAC"])

    def test_Score(self):
        seqs = [MySeq("GTAAACAATATTTATAGC", "dna"), MySeq("AAAATTTACCTCGCAAGG", "dna"), 
                MySeq("CCGTACTGTCAAGCGTGG", "dna"), MySeq("TGAGTAAACGACGTCCCA", "dna"), 
                MySeq("TACTTAACACCCTGTCAA", "dna")]
        teste1 = GibbsSampling(8, seqs)
        offset1 = {"GTAAACAATATTTATAGC": 7, "AAAATTTACCTCGCAAGG": 11, "CCGTACTGTCAAGCGTGG": 9,
                 "TGAGTAAACGACGTCCCA": 4, "TACTTAACACCCTGTCAA": 1}
        self.assertEqual(teste1.Score(offset1), 20)

    def test_prob_para_pos(self):
        seqs = [MySeq("GTAAACAATATTTATAGC", "dna"), MySeq("AAAATTTACCTCGCAAGG", "dna"), 
                MySeq("CCGTACTGTCAAGCGTGG", "dna"), MySeq("TGAGTAAACGACGTCCCA", "dna"), 
                MySeq("TACTTAACACCCTGTCAA", "dna")]
        teste1 = GibbsSampling(8, seqs)
        self.assertEqual(teste1.prob_para_pos("AAAATTTACCTCGCAAGG"), ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0.000732,0.000122,0,0,0,0,0,0.000183,0,0,0]))
                                                                    
    def test_random_selection(self):
        seqs = [MySeq("GTAAACAATATTTATAGC", "dna"), MySeq("AAAATTTACCTCGCAAGG", "dna"), 
                MySeq("CCGTACTGTCAAGCGTGG", "dna"), MySeq("TGAGTAAACGACGTCCCA", "dna"), 
                MySeq("TACTTAACACCCTGTCAA", "dna")]
        teste1 = GibbsSampling(8, seqs)
        offset1 = {"GTAAACAATATTTATAGC": 7, "AAAATTTACCTCGCAAGG": 11, "CCGTACTGTCAAGCGTGG": 9,
                 "TGAGTAAACGACGTCCCA": 4, "TACTTAACACCCTGTCAA": 1}
        self.assertEqual(teste1.RandomSelection(offset1), ("AAAATTTACCTCGCAAGG", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0.000732,0.000122,0,0,0,0,0,0.000183,0,0,0], 0.000732))

    def test_roleta(self):
        seqs = [MySeq("GTAAACAATATTTATAGC", "dna"), MySeq("AAAATTTACCTCGCAAGG", "dna"), 
                MySeq("CCGTACTGTCAAGCGTGG", "dna"), MySeq("TGAGTAAACGACGTCCCA", "dna"), 
                MySeq("TACTTAACACCCTGTCAA", "dna")]
        teste1 = GibbsSampling(8, seqs)
        offset1 = {"GTAAACAATATTTATAGC": 7, "AAAATTTACCTCGCAAGG": 11, "CCGTACTGTCAAGCGTGG": 9,
                 "TGAGTAAACGACGTCCCA": 4, "TACTTAACACCCTGTCAA": 1}
        self.assertEqual(teste1.roleta(offset1), ("AAAATTTACCTCGCAAGG", 0))

    def test_gibbs(self):
        seqs = [MySeq("GTAAACAATATTTATAGC", "dna"), MySeq("AAAATTTACCTCGCAAGG", "dna"), 
                MySeq("CCGTACTGTCAAGCGTGG", "dna"), MySeq("TGAGTAAACGACGTCCCA", "dna"), 
                MySeq("TACTTAACACCCTGTCAA", "dna")]
        teste1 = GibbsSampling(8, seqs)
        self.assertEqual(teste1.gibbs(), ((7,1,9,5,1), ("AATATTTA", "AAAATTTA", "TCAAGCGT", "GTAATCGA", "TACTTCAC")) )

if __name__ == '__main__':
    unittest.main()