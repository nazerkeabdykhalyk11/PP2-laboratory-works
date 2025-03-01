from functools import reduce
from operator import mul
def multiply_all_numbers(numbers):
    return reduce(mul, numbers)

numbers = [2, 3, 4, 5]
result = multiply_all_numbers(numbers)
print(f"Product of all numbers: {result}")
