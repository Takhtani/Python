import re

text = "My phone numbers are 9876543210 and 9123456780. Call before 5 PM."

# 1. match() - checks only at the start of the string
print("match   :", re.match(r"My", text) is not None)

# 2. search() - finds the first occurrence anywhere
m = re.search(r"\d{10}", text)
print("search  :", m.group(), "at position", m.start())

# 3. findall() - returns all occurrences
print("findall :", re.findall(r"\d{10}", text))

# 4. sub() - replaces matches
print("sub     :", re.sub(r"\d{10}", "XXXXXXXXXX", text))

# 5. split() - splits at matches
print("split   :", re.split(r"[ ,.]+", "apple, banana. cherry orange"))

# 6. compile() with a validation pattern
pattern = re.compile(r"^[A-Z][a-z]{2,}\d*$")
for word in ["Python", "python", "Lab26", "Py"]:
    print(f"  {word:8} valid? {bool(pattern.match(word))}")

# 7. groups
date = "Date of practical: 08-11-2026"
g = re.search(r"(\d{2})-(\d{2})-(\d{4})", date)
print("groups  : day =", g.group(1), "month =", g.group(2), "year =", g.group(3))
