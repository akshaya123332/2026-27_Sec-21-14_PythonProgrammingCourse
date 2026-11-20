x = 100  # Global variable

def display():
    x = 50  # Local variable
    print("Inside function:", x)

# Calling the function
display()

print("Outside function:", x)