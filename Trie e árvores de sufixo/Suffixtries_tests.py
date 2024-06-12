import unittest
from suffix_trie import SuffixTrie

class TestSuffixTrie(unittest.TestCase):

    def setUp(self):
        self.trie = SuffixTrie()

    def test_insert_and_exists(self):
        # Testa a inserção de sufixos e verifica se eles existem na SuffixTrie
        words = ["banana", "apple", "cherry"]
        for word in words:
            self.trie.insert_suffix(word)
        
        for word in words:
            self.assertTrue(self.trie.exists(word))

        # Testa com um sufixo que não deve existir
        self.assertFalse(self.trie.exists("pear"))

    def test_delete(self):
        # Testa a deleção de sufixos da SuffixTrie
        words = ["banana", "apple", "cherry"]
        for word in words:
            self.trie.insert_suffix(word)

        self.assertTrue(self.trie.delete("banana"))
        self.assertFalse(self.trie.exists("banana"))

        # Testa com um sufixo que não existe na SuffixTrie
        self.assertFalse(self.trie.delete("pear"))

    def test_find_prefix(self):
        # Testa a função de encontrar prefixos como sufixos na SuffixTrie
        words = ["banana", "apple", "cherry"]
        for word in words:
            self.trie.insert_suffix(word)

        self.assertTrue(self.trie.find_prefix("ban"))
        self.assertTrue(self.trie.find_prefix("a"))
        self.assertFalse(self.trie.find_prefix("pe"))

    def test_to_graphviz(self):
        # Testa a geração do grafo da SuffixTrie usando Graphviz
        words = ["banana", "apple", "cherry"]
        for word in words:
            self.trie.insert_suffix(word)
        graph = self.trie.to_graphviz()
        self.assertIsNotNone(graph)

if __name__ == '__main__':
    unittest.main()
