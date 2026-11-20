def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Taking input from the user
celsius = float(input("Enter temperature in Celsius: "))

# Calling the function
result = celsius_to_fahrenheit(celsius)

# Displaying the result
print("Temperature in Fahrenheit:", result)