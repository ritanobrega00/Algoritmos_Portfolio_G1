import unittest
from bwt import BWT


class TestBWT(unittest.TestCase):
    def setUp(self):
        self.sequences = [
            {"seq": "ATGCGTAGAT", "bwt": "TTG$GATCAGA", "sa": [10, 6, 8, 0, 3, 7, 2, 4, 9, 5, 1],
             "primeira_f": "$AAACGGGTTT",
             "find_occ": ['T1', 'T2', 'G1', '$1', 'G2', 'A1', 'T3', 'C1', 'A2', 'G3', 'A3'],
             "last_to_first": [8, 9, 5, 0, 6, 1, 10, 4, 2, 7, 3], "bw_matching": [9], "bw_matching_pos": [5]},
            {"seq": "CAGTAGCATCG", "bwt": "GTCC$GTCAAGA", "sa": [11, 4, 1, 7, 0, 6, 9, 10, 5, 2, 3, 8],
             "primeira_f": "$AAACCCGGGTT",
             "find_occ": ['G1', 'T1', 'C1', 'C2', '$1', 'G2', 'T2', 'C3', 'A1', 'A2', 'G3', 'A3'],
             "last_to_first": [7, 10, 4, 5, 0, 8, 11, 6, 1, 2, 9, 3], "bw_matching": [10], "bw_matching_pos": [3]},
            {"seq": "TAGCGTAGCT", "bwt": "TTTGGAACC$G", "sa": [10, 1, 6, 3, 8, 2, 7, 4, 9, 0, 5],
             "primeira_f": "$AACCGGGTTT",
             "find_occ": ['T1', 'T2', 'T3', 'G1', 'G2', 'A1', 'A2', 'C1', 'C2', '$1', 'G3'],
             "last_to_first": [8, 9, 10, 5, 6, 1, 2, 3, 4, 0, 7], "bw_matching": [9, 10], "bw_matching_pos": [0, 5]},
        ]

    def test_buildbwt(self):
        for seq in self.sequences:
            bwt = BWT(seq["seq"])
            self.assertEqual(bwt.bwt, seq["bwt"])
            bwt_with_sa = BWT(seq["seq"], sufixarray=True)
            self.assertEqual(bwt_with_sa.bwt, seq["bwt"])
            self.assertEqual(bwt_with_sa.sa, seq["sa"])

    def test_get_first_col(self):
        for seq in self.sequences:
            bwt = BWT(seq["seq"])
            self.assertEqual(bwt.primeira_f, seq["primeira_f"])
            bwt_with_sa = BWT(seq["seq"], sufixarray=True)
            self.assertEqual(bwt_with_sa.primeira_f, seq["primeira_f"])

    def test_find_occ(self):
        for seq in self.sequences:
            bwt = BWT(seq["seq"])
            self.assertEqual(bwt.find_occ(), seq["find_occ"])

    def test_inverse_bwt(self):
        for seq in self.sequences:
            bwt = BWT(seq["seq"])
            self.assertEqual(bwt.inverse_bwt(), seq["seq"] + "$")
            bwt_with_sa = BWT(seq["seq"], sufixarray=True)
            self.assertEqual(bwt_with_sa.inverse_bwt(), seq["seq"] + "$")

    def test_last_to_first(self):
        for seq in self.sequences:
            bwt = BWT(seq["seq"])
            self.assertEqual(bwt.last_to_first(), seq["last_to_first"])

    def test_bw_matching(self):
        for seq in self.sequences:
            bwt = BWT(seq["seq"])
            self.assertEqual(bwt.bw_matching("TAG"), seq["bw_matching"])
            bwt_with_sa = BWT(seq["seq"], sufixarray=True)
            self.assertEqual(bwt_with_sa.bw_matching("TAG"), seq["bw_matching"])

    def test_bw_matching_pos(self):
        for seq in self.sequences:
            bwt_with_sa = BWT(seq["seq"], sufixarray=True)
            self.assertEqual(bwt_with_sa.bw_matching_pos("TAG"), seq["bw_matching_pos"])


if __name__ == '__main__':
    unittest.main()