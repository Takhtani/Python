def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

n = int(input("Enter a number: "))

if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    print(f"Factorial of {n} using loop      = {fact}")
    print(f"Factorial of {n} using recursion = {factorial_recursive(n)}")
