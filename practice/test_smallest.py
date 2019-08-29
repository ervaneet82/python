import unittest
from smallest import noOdds

class TestAdd(unittest.TestCase):
    """
    Test the add function from the mymath library
    """
    def test_noOdds(self):
        """
        Test that the addition of two integers returns the correct total
        """
        self.assertEqual(noOdds([1, 2, 3, 4, 5, 6, 7, 8]), [2, 4, 6, 8])
        self.assertEqual(noOdds([43, 65, 23, 89, 53, 9, 6]), [6])
        self.assertEqual(noOdds([718, 991, 449, 644, 380, 440]), [718, 644, 380, 440])

if __name__ == '__main__':
    unittest.main()