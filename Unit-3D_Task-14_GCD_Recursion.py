def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Taking input from the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Calling the function
result = gcd(a, b)

# Displaying the result
print("GCD of", a, "and", b, "is:", result)