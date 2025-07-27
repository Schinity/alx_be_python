def perform_operations(a, b):
    
    add = lambda x, y: x + y
    subtract = lambda x, y: x - y
    multiply = lambda x, y: x * y
    divide = lambda x, y: x / y if y != 0 else "Division by zero error"

    return {
        "add": add(a, b),
        "subtract": subtract(a, b),
        "multiply": multiply(a, b),
        "divide": divide(a, b)
    }