import pandas as pd
import numpy as np
import io

# 1. From a dictionary of lists
df1 = pd.DataFrame({"Name": ["Aarav", "Diya"], "Marks": [78, 85]})
print("1. From dictionary:\n", df1)

# 2. From a list of lists (with column names)
df2 = pd.DataFrame([["Rohan", 66], ["Sneha", 72]], columns=["Name", "Marks"])
print("\n2. From list of lists:\n", df2)

# 3. From a list of dictionaries
df3 = pd.DataFrame([{"Name": "Kabir", "Marks": 90}, {"Name": "Meera", "Marks": 81}])
print("\n3. From list of dictionaries:\n", df3)

# 4. From a NumPy array
arr = np.array([[1, 2, 3], [4, 5, 6]])
df4 = pd.DataFrame(arr, columns=["A", "B", "C"])
print("\n4. From NumPy array:\n", df4)

# 5. From a Series
s = pd.Series([10, 20, 30], index=["x", "y", "z"], name="Values")
df5 = pd.DataFrame(s)
print("\n5. From Series:\n", df5)

# 6. From a CSV file
csv_text = "Name,City\nAarav,Rajkot\nDiya,Ahmedabad\n"
with open("students.csv", "w") as f:
    f.write(csv_text)
df6 = pd.read_csv("students.csv")
print("\n6. From CSV file:\n", df6)
