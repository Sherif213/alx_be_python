CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9


def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

temp = int(input("Enter the temperature to convert: "))
c_f = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
if c_f == 'F':
    print(f"{temp}°F is {convert_to_celsius(temp)}°C")
elif c_f == 'C':
    print(f"{temp}°C is {convert_to_fahrenheit(temp)}°F")
else:
    print("Invalid input")