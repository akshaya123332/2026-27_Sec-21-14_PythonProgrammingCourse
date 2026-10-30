my_set = {10, 20, 30, 40}

print("Original set:", my_set)

# 1. Membership testing
print("Is 20 present?", 20 in my_set)
print("Is 50 present?", 50 in my_set)

# 2. add()
my_set.add(50)
print("After add:", my_set)

# 3. remove()
my_set.remove(30)
print("After remove:", my_set)

# 4. discard()
my_set.discard(10)
print("After discard:", my_set)