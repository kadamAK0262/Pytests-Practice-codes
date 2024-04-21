from reverse_string import reverse_words

def test_reverse_words():
    # Test case with a simple sentence
    original_string_1 = "Hello World!"
    expected_result_1 = "World! Hello"
    assert reverse_words(original_string_1) == expected_result_1

    # Test case with multiple words and punctuation
    original_string_2 = "Python is awesome."
    expected_result_2 = "awesome. is Python"
    assert reverse_words(original_string_2) == expected_result_2

    # Test case with an empty string
    original_string_3 = ""
    expected_result_3 = ""
    assert reverse_words(original_string_3) == expected_result_3

    # Test case with a single word
    original_string_4 = "Hello"
    expected_result_4 = "Hello"
    assert reverse_words(original_string_4) == expected_result_4

    # Test case with multiple words and spaces
    original_string_5 = "   Hello    World!    "
    expected_result_5 = "World! Hello"
    assert reverse_words(original_string_5) == expected_result_5
