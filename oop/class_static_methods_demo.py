class Calculator:
    """A class demonstrating static and class methods in Python."""

    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method: returns the sum of two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method: prints the calculation type and returns the product."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
