import pytest
from guess_number_game import guess_number

@pytest.mark.parametrize("secret_number, guess, expected", [
    (50, 50, "Congratulations! You guessed the number correctly!"),
    (75, 25, "Too low. Try again."),
    (25, 75, "Too high. Try again."),
])
def test_guess_number(secret_number, guess, expected):
    assert guess_number(secret_number, guess) == expected
