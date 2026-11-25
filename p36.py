import pandas as pd

data = {
    "Name":  ["Aarav", "Diya", "Rohan", "Sneha", "Kabir"],
    "City":  ["Rajkot", "Ahmedabad", "Surat", "Vadodara", "Rajkot"],
    "Marks": [78, 85, 66, 72, 90]
}
df = pd.DataFrame(data)

print("DataFrame:")
print(df)
print("\nShape   :", df.shape)
print("Columns :", list(df.columns))
print("\nSelect 'Marks' column:")
print(df["Marks"])
print("\nStudents with marks > 75:")
print(df[df["Marks"] > 75])
print("\nSorted by Marks (descending):")
print(df.sort_values("Marks", ascending=False))

df["Result"] = df["Marks"].apply(lambda m: "Distinction" if m >= 80 else "Pass")
print("\nAfter adding 'Result' column:")
print(df)
print("\nAverage marks:", df["Marks"].mean())
