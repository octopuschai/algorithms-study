import unittest

from binary_search import binary_search

num_seqs = [3, 99, 7, 14, 65, 21, 17, 31, 26, 72]
string_seqs = ['black', 'red', 'yellow', 'purple', 'gold', 'white', 'grey']


class SearchTest(unittest.TestCase):
    def test_binary_search(self, ):
        self.assertEqual(binary_search(num_seqs, 3), True)
        self.assertEqual(binary_search(num_seqs, 99), True)
        self.assertEqual(binary_search(num_seqs, 26), True)
        self.assertEqual(binary_search(num_seqs, 72), True)
        self.assertEqual(binary_search(num_seqs, 65), True)

        self.assertEqual(binary_search(num_seqs, 0), False)
        self.assertEqual(binary_search(num_seqs, 100), False)

        self.assertEqual(binary_search(string_seqs, 'black'), True)
        self.assertEqual(binary_search(string_seqs, 'red'), True)
        self.assertEqual(binary_search(string_seqs, 'grey'), True)
        self.assertEqual(binary_search(string_seqs, 'white'), True)

        self.assertEqual(binary_search(string_seqs, 'blue'), False)
        self.assertEqual(binary_search(string_seqs, 'green'), False)

        self.assertTrue(binary_search(num_seqs, 26))
        self.assertTrue(binary_search(string_seqs, 'red'))

        self.assertFalse(binary_search(num_seqs, 23))
        self.assertFalse(binary_search(string_seqs, 'blue'))


if __name__ == "__main__":
    unittest.main()
