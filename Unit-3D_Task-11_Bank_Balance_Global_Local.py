balance = 1000  # Global variable

# Function to deposit money
def deposit(amount):
    global balance
    balance = balance + amount
    print("Deposited Amount: ₹", amount)
    print("Updated Balance: ₹", balance)

# Function using a local balance
def local_balance():
    balance = 500  # Local variable
    print("Local Balance: ₹", balance)

# Calling the functions
print("Initial Balance: ₹", balance)

deposit(500)

local_balance()

print("Final Bank Balance: ₹", balance)