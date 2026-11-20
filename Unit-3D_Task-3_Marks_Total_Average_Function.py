def calculate(m1, m2, m3):
    total = m1 + m2 + m3
    average = total / 3
    return total, average

# Taking input from the user
m1 = float(input("Enter marks of subject 1: "))
m2 = float(input("Enter marks of subject 2: "))
m3 = float(input("Enter marks of subject 3: "))

# Calling the function
total, average = calculate(m1, m2, m3)

# Displaying the results
print("Total Marks:", total)
print("Average Marks:", average)