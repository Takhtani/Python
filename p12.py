t = (10, 20, 30, 20, 40, 50)
print("Tuple             :", t)
print("Length            :", len(t))
print("count of 20       :", t.count(20))
print("index of 30       :", t.index(30))
print("Min, Max, Sum     :", min(t), max(t), sum(t))
print("Slice [1:4]       :", t[1:4])
print("Concatenation     :", t + (60, 70))
print("Repetition        :", (1, 2) * 3)
print("40 in tuple?      :", 40 in t)

# converting to list to modify, then back to tuple
temp = list(t)
temp.append(99)
t2 = tuple(temp)
print("After modification:", t2)

# tuple unpacking
a, b, *rest = t
print("Unpacking         :", a, b, rest)

# tuples are immutable
try:
    t[0] = 100
except TypeError as e:
    print("Error:", e)
