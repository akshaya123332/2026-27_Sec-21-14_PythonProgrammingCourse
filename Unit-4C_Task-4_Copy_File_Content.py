try:
    file1 = open("sample.txt", "r")
    content = file1.read()
    file1.close()

    file2 = open("copy.txt", "w")
    file2.write(content)
    file2.close()

    print("File copied successfully.")

except FileNotFoundError:
    print("Error: sample.txt not found.")