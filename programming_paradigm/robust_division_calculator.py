def safe_divide(numerator, denominator):
    try:
        # Convert command line arguments to floats
        numerator = float(numerator)
        denominator = float(denominator)
        result = numerator / denominator
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except ValueError:
        return "Error: Please enter numeric values only."
    else:
        return f"The result of the division is {result:.1f}"
