def find_min_sum_of_factors(number):
    min_sum = 0

    for i in range(2, int(number**0.5) + 1):
        while number % i == 0:
            min_sum += i
            number //= i

    if number > 1:
        min_sum += number

    return min_sum
