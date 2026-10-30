my_list = [10, 20, 30, 20, 40, 10, 50]

print("Original list:", my_list)

# Convert list into a set to remove duplicates
new_set = set(my_list)

# Convert set back into a list
new_list = list(new_set)

print("List after removing duplicates:", new_list)