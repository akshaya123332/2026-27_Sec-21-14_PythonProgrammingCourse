count = 0  # Global variable

def increment():
    global count
    count = count + 1
    print("Counter inside function:", count)

# Calling the function
increment()
increment()
increment()

print("Final Counter:", count)