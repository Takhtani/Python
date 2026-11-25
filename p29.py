import os

# 1. Create and write to a file
with open("students.txt", "w") as f:
    f.write("Aarav\n")
    f.write("Diya\n")
    f.write("Rohan\n")
print("File created and written.")

# 2. Read the whole file
with open("students.txt", "r") as f:
    print("\nread() ->")
    print(f.read())

# 3. Read line by line
with open("students.txt", "r") as f:
    print("readline() ->", f.readline().strip())
    print("readlines() ->", f.readlines())

# 4. Append to the file
with open("students.txt", "a") as f:
    f.write("Meera\n")
print("\nAfter appending:")
with open("students.txt") as f:
    for line in f:
        print(" ", line.strip())

# 5. File information and deletion
print("\nFile exists?", os.path.exists("students.txt"))
print("File size (bytes):", os.path.getsize("students.txt"))
os.remove("students.txt")
print("File deleted. Exists now?", os.path.exists("students.txt"))
