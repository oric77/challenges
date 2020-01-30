import unittest
from data import DICTIONARY, LETTER_SCORES, POUCH
import game


class MyTestCase(unittest.TestCase):
    def test_split_by_len(self):
        dict_by_len = game.split_by_len()

        for k, i in dict_by_len.items():
            # each list string length equals its key
            self.assertEqual(k, len(i[0]))
            # each list has words of single length
            self.assertEqual(1, len(set([len(word) for word in i])))

        # total elements in list equals elements in original list
        self.assertEqual(len(DICTIONARY), sum([len(l) for l in dict_by_len.values()]))


if __name__ == '__main__':
    unittest.main()
