import unittest
from exercise4 import chunking_by

class TestDuplicateOdds(unittest.TestCase):
    
    def test_chunking_by(self):

        # list with odd numbers and zero
        self.assertEqual(chunking_by([5, 4, 7, 3, 4, 5, 4], 3), [[5, 4, 7], [3, 4, 5], [4]])
        self.assertEqual(chunking_by([3, 4, 5], 1), [[3], [4], [5]])
        
if __name__ == '__main__':
    unittest.main()