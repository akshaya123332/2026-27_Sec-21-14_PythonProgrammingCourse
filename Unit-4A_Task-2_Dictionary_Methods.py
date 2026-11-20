# Creating a dictionary
student = {
    "name": "Krishna",
    "age": 20,
    "course": "CSE"
}

# Using keys()
print("Keys:", student.keys())

# Using values()
print("Values:", student.values())

# Using items()
print("Items:", student.items())

# Using get()
print("Name:", student.get("name"))

# Using update()
student.update({"age": 21, "city": "Guntur"})
print("After Update:", student)

# Using pop()
student.pop("course")
print("After Pop:", student)