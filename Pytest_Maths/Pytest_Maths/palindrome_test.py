import pytest
from palindrome import is_palindrome

@pytest.mark.parametrize("number, expected", [
    (121, True),
    (12321, True),
    (12345, False),
    (1001, True),
    (12345678987654321, True),
])
def test_is_palindrome(number, expected):
    assert is_palindrome(number) == expected
