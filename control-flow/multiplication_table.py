number = int(input("Enter a number to see its multiplication table:"))
for Y in range(1, 11):
    X = number
    Z = number * Y
    print(f"{X} x {Y} = {Z}")