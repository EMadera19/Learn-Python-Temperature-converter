# Python Temperature Conversion

unit = input("is this temperature in Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))

# Fahrenheit Conversion
if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The Temperature in Fahrenheit is: {temp}°F")

# Celsius Conversion
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The Temperature in Celsius is: {temp}°C")

else:
    print(f"{unit} is not a valid unit of measurement")
