# Taking input from the user
sentence = input("Enter a sentence: ")

# Creating an empty dictionary
word_count = {}

# Splitting the sentence into words
words = sentence.split()

# Counting word frequency
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Displaying the result
print("Word Frequency:")
for word, count in word_count.items():
    print(word, ":", count)