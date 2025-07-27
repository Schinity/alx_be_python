def perform_operations(num1, num2, operation):
    add = lambda x, y: x + y
    subtract = lambda x, y: x - y
    multiply = lambda x, y: x * y
    divide = lambda x, y: x / y if y != 0 else "Division by zero error"

    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide
    }

    if operation in operations:
        return operations[operation](num1, num2)
    else:
        return "Invalid operation"