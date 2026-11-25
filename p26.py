for attempt in (1, 2):
    print(f"--- Attempt {attempt} ---")
    try:
        a = int(input("Enter numerator: "))
        b = int(input("Enter denominator: "))
        result = a / b
    except ZeroDivisionError:
        print("Except block: cannot divide by zero.")
    else:
        print("Else block: division successful, result =", result)
