# Objective: Implement a division calculator that robustly handles errors like division
#  by zero and non-numeric inputs using command line arguments.


def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)

        if denom == 0:
            return "Error: Cannot divide by zero."

        result = num / denom
        return f"The result of the division is {result}"
    except ValueError:
        return "Error: Please enter numeric values only."