# Creating squares of numbers from 1 to 10
squares = [x**2 for x in range(1, 11)]

# Creating a list of even numbers from 1 to 10
even_numbers = [x for x in range(1, 11) if x % 2 == 0]

# Displaying the results
print("Squares:", squares)
print("Even Numbers:", even_numbers)