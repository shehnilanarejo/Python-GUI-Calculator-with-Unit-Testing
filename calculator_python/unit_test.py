# test_calculator.py

import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(10, 5), 15)
    
    def test_subtract(self):
        self.assertNotEqual(calculator.subtract(10, 5), 10)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(3, 7), 21)

    def test_divide(self):
        self.assertAlmostEqual(calculator.divide(10, 3), 3.333333, places=4)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            calculator.divide(5, 0)

    def test_type(self):
        self.assertIsInstance(calculator.add(1, 2), int)

if __name__ == '__main__':
    unittest.main()

