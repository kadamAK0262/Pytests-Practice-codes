user_input = "Akshay"

def remove_duplicates(input_string):
    seen_chars = set()
    result_string = ''

    for char in input_string:
        if char not in seen_chars:
            seen_chars.add(char)
            result_string += char

    return result_string


result = remove_duplicates(user_input)

print(f"String after removing duplicates: {result}")
