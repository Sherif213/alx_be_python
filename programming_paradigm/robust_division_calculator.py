def safe_divide(numerator, denominator):
    try:
        float(numerator)/float(denominator)
    except ValueError:
        print("Error: Please enter numeric values only.")
    try:
        numerator/denominator
    except ZeroDivisionError:
        print(f"Error: Cannot divide by zero.")