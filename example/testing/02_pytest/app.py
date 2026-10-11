def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ValueError("На нуль ділити не можна")
    return a / b


def is_even(number):
    return number % 2 == 0


def get_positive_numbers(numbers):
    return [number for number in numbers if number > 0]