def calculate_sum(*args):
    total = 0
    for i in args:
        total = total + i
    return total

# Calling the function
result = calculate_sum(10, 20, 30, 40, 50)

# Displaying the result
print("Sum of Values:", result)