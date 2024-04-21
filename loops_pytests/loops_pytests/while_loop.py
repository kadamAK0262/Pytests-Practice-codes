# factorial

def calculate_factorial(n):
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result


# fibonacci_series

def generate_fibonacci_series(limit):
    fibonacci_series = [0, 1]
    while fibonacci_series[-1] + fibonacci_series[-2] <= limit:
        fibonacci_series.append(fibonacci_series[-1] + fibonacci_series[-2])
    return fibonacci_series
