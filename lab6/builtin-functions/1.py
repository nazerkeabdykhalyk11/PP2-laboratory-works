from functools import reduce

def multiply_all_numbers(numbers):
    return reduce(lambda x, y: x * y, numbers)

numbers = [2, 3, 4, 5]
result = multiply_all_numbers(numbers)
print(f"Product of all numbers: {result}")
