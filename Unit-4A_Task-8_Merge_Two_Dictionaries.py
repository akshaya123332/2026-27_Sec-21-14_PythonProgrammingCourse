# Creating two dictionaries
dict1 = {"a": 10, "b": 20}
dict2 = {"c": 30, "d": 40}

# Creating a copy of the first dictionary
merged = dict1.copy()

# Merging the second dictionary
merged.update(dict2)

# Displaying the dictionaries
print("First Dictionary:", dict1)
print("Second Dictionary:", dict2)
print("Merged Dictionary:", merged)