import math
import random
import datetime
import calendar
from statistics import mean
import math as m

# 1. math module
print("sqrt(144) =", math.sqrt(144))
print("pi        =", math.pi)
print("factorial(5) =", math.factorial(5))
print("ceil(4.2), floor(4.8) =", math.ceil(4.2), math.floor(4.8))

# 2. random module (seed fixed so output repeats)
random.seed(10)
print("Random number between 1 and 100:", random.randint(1, 100))
print("Random choice:", random.choice(["red", "green", "blue"]))

# 3. datetime module
d = datetime.date(2026, 11, 8)
print("Date:", d, "| Day:", d.strftime("%A"))
print("After 30 days:", d + datetime.timedelta(days=30))

# 4. calendar and statistics modules
print("Is 2028 a leap year?", calendar.isleap(2028))
print("Mean of [10, 20, 30, 40] =", mean([10, 20, 30, 40]))
print("Using alias: m.pow(2, 5) =", m.pow(2, 5))

# 5. user-defined module (created here and then imported)
with open("mymath.py", "w") as f:
    f.write("def square(n):\n    return n * n\n\n")
    f.write("def cube(n):\n    return n * n * n\n")

import mymath
print("mymath.square(6) =", mymath.square(6))
print("mymath.cube(3)   =", mymath.cube(3))
