import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

numbers = [10, 23, 35, 47, 4, 51, 2, 9]
prime_numbers = filter_prime(numbers)
print("Prime numbers:", prime_numbers)