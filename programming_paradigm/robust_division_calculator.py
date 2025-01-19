def safe_divide(numerator, denominator):
    try:
        numerator/denominator
    except ZeroDivisionError:
        print(f"Error: Cannot divide by zero.")