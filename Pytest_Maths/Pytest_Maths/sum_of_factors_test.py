import pytest
from sum_of_factors import find_min_sum_of_factors

@pytest.mark.parametrize("number, expected", [
    (12, 7),  # Factors: 2, 2, 3. Min sum: 2 + 3 + 2 = 7
    (30, 10), # Factors: 2, 3, 5. Min sum: 2 + 3 + 5 = 10
    (100, 14),# Factors: 2, 2, 5, 5. Min sum: 2 + 2 + 5 + 5 = 14
    (7, 7),   # Prime number, sum is the number itself
    (1, 0),   # Number 1 has no proper factors, sum is 0
])
def test_find_min_sum_of_factors(number, expected):
    assert find_min_sum_of_factors(number) == expected
