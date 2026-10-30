text = input("Enter a string: ")
reverse = text[::-1]
if text == reverse:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")