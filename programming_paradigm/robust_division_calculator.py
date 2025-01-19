def safe_divide(numerator, denominator):
    try:
        float(numerator)/float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."
    try:
        numerator/denominator
    except ZeroDivisionError:
        return f"Error: Cannot divide by zero."
        
    return f"The result of the division is {numerator/denominator}"