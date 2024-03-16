import unittest
from exercise2 import index_power

class TestDuplicateOdds(unittest.TestCase):
    
    def test_index_power(self):

        self.assertEqual(index_power([1, 2, 3, 4], 2), 9)
        self.assertEqual(index_power([1, 3, 10, 100], 3), 1000000)
        self.assertEqual(index_power([0, 1], 0), 1)
        self.assertEqual(index_power([1, 2], 3), -1)
        

if __name__ == '__main__':
    unittest.main()