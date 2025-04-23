"""Basic tests for my_package"""

import unittest
from my_package.module2 import add_numbers, multiply_numbers

class TestBasicFunctions(unittest.TestCase):
    """Test class for basic functions"""
    
    def test_add_numbers(self):
        """Test the add_numbers function"""
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(0, 0), 0)
    
    def test_multiply_numbers(self):
        """Test the multiply_numbers function"""
        self.assertEqual(multiply_numbers(2, 3), 6)
        self.assertEqual(multiply_numbers(-1, 1), -1)
        self.assertEqual(multiply_numbers(0, 5), 0)

if __name__ == "__main__":
    unittest.main()
