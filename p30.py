# 'w' - write mode (creates the file or overwrites it)
with open("demo.txt", "w") as f:
    f.write("Line 1: written in w mode\n")
print("w  :", open("demo.txt").read().strip())

# 'a' - append mode (adds at the end)
with open("demo.txt", "a") as f:
    f.write("Line 2: added in a mode\n")
print("a  :", open("demo.txt").read().strip().replace("\n", " | "))

# 'r' - read mode (default)
with open("demo.txt", "r") as f:
    print("r  : first line ->", f.readline().strip())

# 'r+' - read and write
with open("demo.txt", "r+") as f:
    content = f.read()
    f.write("Line 3: added in r+ mode\n")
print("r+ :", open("demo.txt").read().strip().replace("\n", " | "))

# 'x' - exclusive creation (error if file already exists)
try:
    open("demo.txt", "x")
except FileExistsError:
    print("x  : FileExistsError - demo.txt already exists")

# 'wb' and 'rb' - binary modes
with open("demo.bin", "wb") as f:
    f.write(bytes([65, 66, 67, 68]))
with open("demo.bin", "rb") as f:
    data = f.read()
print("wb/rb:", data, "->", list(data))

import os
os.remove("demo.txt")
os.remove("demo.bin")
