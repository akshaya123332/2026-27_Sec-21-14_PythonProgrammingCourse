def student_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

# Calling the function
student_details(name="Krishna", Python=90, Java=85, Maths=95)