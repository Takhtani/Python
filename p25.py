while True:
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError:
        print("Invalid input! Please enter a whole number.")

print("Your age is", age)
