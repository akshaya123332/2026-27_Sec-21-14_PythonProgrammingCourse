# Creating a subject-marks dictionary
subjects = {
    "Python": 90,
    "Java": 85,
    "Maths": 95,
    "English": 80
}

# Printing keys using loop
print("Subject Names:")
for key in subjects.keys():
    print(key)

# Printing values using loop
print("\nSubject Marks:")
for value in subjects.values():
    print(value)

# Printing items using loop
print("\nSubject and Marks:")
for key, value in subjects.items():
    print(key, ":", value)