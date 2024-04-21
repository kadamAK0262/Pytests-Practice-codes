original_string = "Hello World! Python is awesome."

def reverse_words(input_string):
    # Split the string into a list of words
    words = input_string.split()
    reversed_words = words[::-1]
    reversed_string = ' '.join(reversed_words)

    return reversed_string


result = reverse_words(original_string)

print("Original string:", original_string)
print("Reversed string:", result)
