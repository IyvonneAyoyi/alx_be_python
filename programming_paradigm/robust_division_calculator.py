def safe_divide(numerator, denominator):
    """
    Performs division of two numbers with error handling.
    Returns the division result or an appropriate error message.
    """
    try:
        # Convert inputs to floats
        num = float(numerator)
        den = float(denominator)

        # Try division
        result = num / den
        return f"The result of the division is {result}"
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    except ValueError:
        return "Error: Please enter numeric values only."
