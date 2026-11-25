try:
    a = int(input("Enter the numerator: "))
    b = int(input("Enter the denominator: "))
    result = a / b
    print("Result =", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

print("Program continues to run after handling the error.")
