def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Taking input from the user
n = int(input("Enter the number of terms: "))

# Generating Fibonacci series
print("Fibonacci Series:")
for i in range(n):
    print(fibonacci(i), end=" ")