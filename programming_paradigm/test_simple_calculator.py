# programming_paradigm/test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Set up the calculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test various cases for addition."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-2, -3), -5)
        self.assertAlmostEqual(self.calc.add(2.5, 3.1), 5.6)

    def test_subtraction(self):
        """Test various cases for subtraction."""
        self.assertEqual(self.calc.subtract(10, 3), 7)
        self.assertEqual(self.calc.subtract(3, 10), -7)
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.2), 3.3)

    def test_multiply(self):
        """Test various cases for multiplication."""
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(-3, 4), -12)
        self.assertEqual(self.calc.multiply(-3, -4), 12)
        self.assertAlmostEqual(self.calc.multiply(2.5, 2), 5.0)

    def test_divide(self):
        """Test various cases for division."""
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertIsInstance(self.calc.divide(7, 2), float)
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertEqual(self.calc.divide(-10, 2), -5.0)
        self.assertEqual(self.calc.divide(-10, -2), 5.0)
        self.assertAlmostEqual(self.calc.divide(5.5, 2.2), 2.5)

if __name__ == "__main__":
    unittest.main()
