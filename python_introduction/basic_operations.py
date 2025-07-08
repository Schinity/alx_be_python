# basic arithmetic operations

# numbers input
# This program performs basic arithmetic operations on two numbers provided by the user.
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))   

# arithmetic operations

sum = number1 + number2
difference = number1 - number2
product = number1 * number2

# division by zero check
if number2 != 0:
    quotient = number1 / number2
else:
    quotient = "Error: Division by zero"

# display results
print(f"Addition of {number1} and {number2} is {sum}")
print(f"Subtraction of {number1} and {number2} is {difference}")
print(f"Multiplication of {number1} and {number2} is {product}")
print(f"Quotient of {number1} and {number2} is {quotient}")
