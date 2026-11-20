# Creating a nested dictionary
students = {
    1: {"name": "Krishna", "marks": 90},
    2: {"name": "Rahul", "marks": 85},
    3: {"name": "Priya", "marks": 95}
}

# Printing student details
for roll_no, details in students.items():
    print("Roll Number:", roll_no)
    print("Name:", details["name"])
    print("Marks:", details["marks"])
    print()