my_list = [10, 20, 30, 20, 40, 10, 50]

new_list = []

for item in my_list:
    if item not in new_list:
        new_list.append(item)

print("Original list:", my_list)
print("List after removing duplicates:", new_list)