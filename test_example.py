# test_example.py

import unittest

# A simple function to test.
def add(a, b):
    return a + b

# A test class that inherits from unittest.TestCase.
# This is a standard way to write tests in Python.
class TestMyFunctions(unittest.TestCase):
    
    # Each method that starts with `test_` is a separate test.
    def test_add_positive_numbers(self):
        """
        Tests the add function with two positive numbers.
        """
        # The 'assertEqual' method checks if the first argument equals the second.
        self.assertEqual(add(1, 2), 3)

    def test_add_negative_numbers(self):
        """
        Tests the add function with two negative numbers.
        """
        self.assertEqual(add(-1, -1), -2)

    def test_add_zero(self):
        """
        Tests the add function with zero.
        """
        self.assertEqual(add(5, 0), 5)

# This block allows you to run the tests directly from the command line.
if __name__ == '__main__':
    unittest.main()

