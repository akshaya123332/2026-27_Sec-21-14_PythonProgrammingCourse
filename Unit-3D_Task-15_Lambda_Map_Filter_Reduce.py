from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

# Using map() to find squares
squares = list(map(lambda x: x * x, numbers))
print("Squares:", squares)

# Using filter() to find even numbers
even = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers:", even)

# Using reduce() to find the sum
total = reduce(lambda x, y: x + y, numbers)
print("Sum of Numbers:", total)