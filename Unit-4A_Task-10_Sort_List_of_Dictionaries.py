# Creating a list of student dictionaries
students = [
    {"name": "Krishna", "marks": 85},
    {"name": "Rahul", "marks": 90},
    {"name": "Priya", "marks": 75},
    {"name": "Anu", "marks": 95}
]

# Sorting in ascending order
ascending = sorted(students, key=lambda x: x["marks"])

print("Ascending Order:")
for student in ascending:
    print(student)

# Sorting in descending order
descending = sorted(students, key=lambda x: x["marks"], reverse=True)

print("\nDescending Order:")
for student in descending:
    print(student)