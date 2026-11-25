# Function without return value
def greet(name):
    print(f"Hello, {name}! Welcome to the Python lab.")

# Function with return value
def calculate_simple_interest(principal, rate, time):
    """Return the simple interest for the given values."""
    return (principal * rate * time) / 100

# Function returning a boolean
def is_even(n):
    return n % 2 == 0

# Function returning multiple values
def min_max(numbers):
    return min(numbers), max(numbers)

greet("Student")
si = calculate_simple_interest(10000, 5, 2)
print("Simple interest on 10000 at 5% for 2 years =", si)
print("Is 14 even?", is_even(14))
print("Is 7 even?", is_even(7))
low, high = min_max([45, 12, 78, 33])
print("Smallest and largest:", low, high)
print("Docstring:", calculate_simple_interest.__doc__)
