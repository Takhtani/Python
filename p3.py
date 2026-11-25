a0 = int(input("Enter value of a: "))
b0 = int(input("Enter value of b: "))
print("Before swapping: a =", a0, ", b =", b0)

# Method 1: using a temporary variable
a, b = a0, b0
temp = a
a = b
b = temp
print("Method 1 (temp variable)   : a =", a, ", b =", b)

# Method 2: using tuple unpacking
a, b = a0, b0
a, b = b, a
print("Method 2 (tuple unpacking) : a =", a, ", b =", b)

# Method 3: using arithmetic operators
a, b = a0, b0
a = a + b
b = a - b
a = a - b
print("Method 3 (arithmetic)      : a =", a, ", b =", b)
