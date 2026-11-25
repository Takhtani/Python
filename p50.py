import os

folder = "demo_folder"
os.makedirs(folder, exist_ok=True)

# create some sample files
for name in ["notes.txt", "report.pdf", "data.csv"]:
    with open(os.path.join(folder, name), "w") as f:
        f.write("sample content for " + name)
os.makedirs(os.path.join(folder, "images"), exist_ok=True)

print("Contents of", folder + ":")
for item in sorted(os.listdir(folder)):
    path = os.path.join(folder, item)
    kind = "File     " if os.path.isfile(path) else "Directory"
    size = os.path.getsize(path) if os.path.isfile(path) else "-"
    print(f"  {kind}  {item:12} size: {size}")

check = input("\nEnter file name to check: ")
if os.path.exists(os.path.join(folder, check)):
    print(check, "exists in the directory.")
else:
    print(check, "does NOT exist in the directory.")
