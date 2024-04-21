def sum_elements(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


# vowels_consonants

def find_vowels_and_consonants(input_string):
    vowels = "aeiouAEIOU"
    input_string = input_string.replace(" ", "")  # Remove spaces

    vowel_count = sum(1 for char in input_string if char in vowels)
    consonant_count = len(input_string) - vowel_count

    return vowel_count, consonant_count
