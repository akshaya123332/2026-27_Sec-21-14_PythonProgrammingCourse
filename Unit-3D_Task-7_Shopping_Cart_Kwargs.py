def shopping_cart(**products):
    total = 0

    for item, price in products.items():
        print(item, ": ₹", price)
        total = total + price

    print("Total Amount: ₹", total)

# Calling the function
shopping_cart(apple=15, orange=12, mango=10)