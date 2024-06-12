import unittest
from Gibs_sampling import GibsSampling

class TestGibsSampling(unittest.TestCase):  
    def setUp(self):
        self.seqs = ["GTAAACAATATTTATAGC", "AAAATTTACCTCGCAAGG", 
            "CCGTACTGTCAAGCGTGG", "TGAGTAAACGACGTCCCA", 
            "TACTTAACACCCTGTCAA"]
        self.gibs = GibsSampling(8, self.seqs)
        self.gibs_2 = GibsSampling(4, self.seqs)
    
    def test_len(self):
        self.assertEqual(len(self.gibs), 5)
        self.assertEqual(len(self.gibs_2), 5)
        self.assertNotEqual(len(self.gibs_2), 4)
    
    def test_getitem(self):
        for i in range(len(self.gibs)):
            self.assertEqual(self.gibs[i], self.seqs[i])
        for i in range(len(self.gibs_2)):    
            self.assertEqual(self.gibs_2[i], self.seqs[i])

    def test_seqSize(self):
        for i in range(len(self.gibs)):
            self.assertNotEqual(self.gibs.seqSize(i), 20)
            self.assertEqual(self.gibs.seqSize(i), 18) 
            self.assertEqual(self.gibs_2.seqSize(i), 18)
            self.assertNotEqual(self.gibs_2.seqSize(i), 2)

    def test_RandomOffsets(self):
        offsets = self.gibs.RandomOffsets()
        self.assertEqual(len(offsets), 5)
        for seq, offset in offsets.items():
            self.assertTrue(0 <= offset < len(seq) - self.gibs.motifSize + 1)
            self.assertEqual(type(seq), str)
            self.assertEqual(type(offset), int)
        offsets_2 = self.gibs_2.RandomOffsets()
        self.assertEqual(len(offsets), 5)
        for seq, offset in offsets_2.items():
            self.assertTrue(0 <= offset < len(seq) - self.gibs_2.motifSize + 1)

    def test_CreateMotifs(self):
        offsets = self.gibs.RandomOffsets()
        motifs = self.gibs.CreateMotifs(offsets)
        for motif in motifs:
            self.assertEqual(len(motif), 8)
            self.assertEqual(type(motif), str)
        offsets2 = self.gibs_2.RandomOffsets()
        motifs2 = self.gibs_2.CreateMotifs(offsets2)
        self.assertEqual(type(motifs), list)
        for motif in motifs2:
            self.assertEqual(len(motif), 4)
            self.assertNotEqual(len(motif), 8)
            self.assertTrue(isinstance(motif, str))

    def test_Score(self):
        offsets2 = self.gibs_2.RandomOffsets()
        score = self.gibs_2.Score(offsets2)
        self.assertTrue(isinstance(score, float))

    def test_prob_para_pos(self):
        seq = self.seqs[0]
        probabilidades = self.gibs.prob_para_pos(seq)
        probabilidades2 = self.gibs_2.prob_para_pos(seq)
        self.assertEqual(len(probabilidades), len(seq) - self.gibs.motifSize + 1)
        self.assertEqual(len(probabilidades2), len(seq) - self.gibs_2.motifSize + 1)
        self.assertAlmostEqual(sum(probabilidades.values()), 1.0, places=6)

    def test_RandomSelection(self):
        offsets = self.gibs.RandomOffsets()
        seq, probabilidades, cutoff = self.gibs.RandomSelection(offsets)
        self.assertIn(seq, self.seqs)
        self.assertTrue(0 <= cutoff <= 1)
        self.assertEqual(len(probabilidades), len(seq) - self.gibs.motifSize + 1)
        self.assertEqual(type(seq), str)
        self.assertEqual(type(cutoff), float)
        self.assertEqual(type(probabilidades), dict)
        offsets2 = self.gibs_2.RandomOffsets()
        seq2, probabilidades2, cutoff2 = self.gibs_2.RandomSelection(offsets2)
        self.assertIn(seq2, self.seqs)
        self.assertTrue(0 <= cutoff2 <= 1)
        self.assertEqual(len(probabilidades2), len(seq2) - self.gibs_2.motifSize + 1)

    def test_Roleta(self):
        offsets = self.gibs.RandomOffsets()
        seq, pos = self.gibs.Roleta(offsets)
        self.assertIn(seq, self.seqs)
        self.assertTrue(0 <= pos < len(seq) - self.gibs.motifSize + 1)
        self.assertEqual(type(seq), str)
        self.assertEqual(type(pos), int)
        offsets2 = self.gibs_2.RandomOffsets()
        seq2, pos2 = self.gibs_2.Roleta(offsets2)
        self.assertIn(seq2, self.seqs)
        self.assertTrue(0 <= pos2 < len(seq2) - self.gibs_2.motifSize + 1)

    def test_Gibs(self):
        best_offsets, best_motifs = self.gibs.Gibs()
        self.assertEqual(len(best_offsets), len(self.seqs))
        self.assertEqual(len(best_motifs), len(self.seqs))
        self.assertEqual(type(best_offsets), dict)
        self.assertEqual(type(best_motifs), list)
        best_offsets2, best_motifs2 = self.gibs_2.Gibs()
        self.assertEqual(len(best_offsets2), len(self.seqs))
        self.assertEqual(len(best_motifs2), len(self.seqs))
        self.assertEqual(type(best_offsets2), dict)
        self.assertEqual(type(best_motifs2), list)

if __name__ == '__main__':
    unittest.main()