def student_info(name, age, city="Rajkot"):
    print(f"Name: {name}, Age: {age}, City: {city}")

def add_all(*args):
    return sum(args)

def show_details(**kwargs):
    for key, value in kwargs.items():
        print(f"  {key} = {value}")

def mixed(a, b=10, *args, **kwargs):
    print("a =", a, "| b =", b, "| args =", args, "| kwargs =", kwargs)

print("1. Positional arguments:")
student_info("Aarav", 21)

print("2. Keyword arguments (order does not matter):")
student_info(age=22, name="Diya")

print("3. Default argument overridden:")
student_info("Rohan", 23, "Surat")

print("4. Variable-length arguments (*args):")
print("  Sum =", add_all(1, 2, 3, 4, 5))

print("5. Keyword variable-length arguments (**kwargs):")
show_details(name="Meera", course="CS&CL", semester=1)

print("6. Mixed arguments:")
mixed(1)
mixed(1, 2, 3, 4, x=5, y=6)
