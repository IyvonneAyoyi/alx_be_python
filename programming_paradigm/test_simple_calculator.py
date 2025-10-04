import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Set up the calculator instance before each test."""
        self.calc = SimpleCalculator()

    # ---------- Addition Tests ----------
    def test_addition_positive_numbers(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(100, 50), 150)

    def test_addition_with_negative_numbers(self):
        self.assertEqual(self.calc.add(-2, -3), -5)
        self.assertEqual(self.calc.add(-5, 5), 0)

    def test_addition_with_floats(self):
        self.assertAlmostEqual(self.calc.add(2.5, 3.1), 5.6)

    # ---------- Subtraction Tests ----------
    def test_subtraction_positive_numbers(self):
        self.assertEqual(self.calc.subtract(10, 3), 7)

    def test_subtraction_negative_result(self):
        self.assertEqual(self.calc.subtract(3, 10), -7)

    def test_subtraction_with_floats(self):
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.2), 3.3)

    # ---------- Multiplication Tests ----------
    def test_multiplication_positive_numbers(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)

    def test_multiplication_with_zero(self):
        self.assertEqual(self.calc.multiply(5, 0), 0)

    def test_multiplication_with_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-3, 4), -12)
        self.assertEqual(self.calc.multiply(-3, -4), 12)

    def test_multiplication_with_floats(self):
        self.assertAlmostEqual(self.calc.multiply(2.5, 2), 5.0)

    # ---------- Division Tests ----------
    def test_division_positive_numbers(self):
        self.assertEqual(self.calc.divide(10, 2), 5.0)

    def test_division_result_is_float(self):
        self.assertIsInstance(self.calc.divide(7, 2), float)

    def test_division_by_zero(self):
        self.assertIsNone(self.calc.divide(10, 0))

    def test_division_negative_numbers(self):
        self.assertEqual(self.calc.divide(-10, 2), -5.0)
        self.assertEqual(self.calc.divide(-10, -2), 5.0)

    def test_division_with_floats(self):
        self.assertAlmostEqual(self.calc.divide(5.5, 2.2), 2.5)

if __name__ == "__main__":
    unittest.main()
