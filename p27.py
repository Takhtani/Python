for attempt in (1, 2):
    print(f"--- Attempt {attempt} ---")
    try:
        a = int(input("Enter numerator: "))
        b = int(input("Enter denominator: "))
        print("Result =", a / b)
    except ZeroDivisionError:
        print("Except block: cannot divide by zero.")
    finally:
        print("Finally block: this always executes.")
