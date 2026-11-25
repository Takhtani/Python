s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

print("Using + operator :", s1 + s2)
print("With a space     :", s1 + " " + s2)
print("Using join()     :", " ".join([s1, s2]))
print("Using f-string   :", f"{s1} {s2}")
