import unittest
from exercise1 import replace_last

class TestDuplicateOdds(unittest.TestCase):
    
    def test_replace_last(self):

        self.assertEqual(replace_last([2, 3, 4, 1]), [1, 2, 3, 4])
        self.assertEqual(replace_last([1, 2, 3, 4]), [4, 1, 2, 3])
        self.assertEqual(replace_last([1]), [1])
        self.assertEqual(replace_last([]), [])
        

if __name__ == '__main__':
    unittest.main()