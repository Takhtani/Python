class Calculator:
    # Python does not support true overloading, so a default
    # argument is used to allow 2 or 3 arguments.
    def add(self, a, b, c=0):
        return a + b + c

calc = Calculator()
print("Sum of two numbers   : add(10, 20)     =", calc.add(10, 20))
print("Sum of three numbers : add(10, 20, 30) =", calc.add(10, 20, 30))


# Second approach: variable-length arguments
class Calculator2:
    def add(self, *args):
        return sum(args)

calc2 = Calculator2()
print("\nUsing *args:")
print("add(5, 6)          =", calc2.add(5, 6))
print("add(5, 6, 7)       =", calc2.add(5, 6, 7))
print("add(1, 2, 3, 4, 5) =", calc2.add(1, 2, 3, 4, 5))
