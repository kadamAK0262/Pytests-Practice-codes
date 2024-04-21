def find_vowels_consonants(input_string):
    vowels = "AEIOUaeiou"
    consonants = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"

    vowel_count = sum(1 for char in input_string if char in vowels)
    consonant_count = sum(1 for char in input_string if char in consonants)

    return vowel_count, consonant_count




# def find_vowels_consonants(input_string):
#     vowels = "AEIOUaeiou"
#     consonants = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"

#     # Filter out special characters and spaces
#     filtered_input = ''.join(char for char in input_string if char.isalnum())

#     vowel_count = sum(1 for char in filtered_input if char in vowels)
#     consonant_count = sum(1 for char in filtered_input if char in consonants)

#     return vowel_count, consonant_count