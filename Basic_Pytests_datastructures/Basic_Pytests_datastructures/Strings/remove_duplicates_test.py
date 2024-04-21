from remove_duplicates import remove_duplicates

def test_remove_duplicates_no_duplicates():
    input_string = "abcde"
    expected_result = "abcde"
    assert remove_duplicates(input_string) == expected_result

def test_remove_duplicates_all_duplicates():
    input_string = "aaaaa"
    expected_result = "a"
    assert remove_duplicates(input_string) == expected_result

def test_remove_duplicates_empty_string():
    input_string = ""
    expected_result = ""
    assert remove_duplicates(input_string) == expected_result

def test_remove_duplicates_mixed_characters():
    input_string = "hello world"
    expected_result = "helo wrd"
    assert remove_duplicates(input_string) == expected_result
