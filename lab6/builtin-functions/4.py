import time
import math

def delayed_square_root(number, delay_ms):
    time.sleep(delay_ms / 1000.0)
    return math.sqrt(number)

number = int(input("Enter number: "))
delay_ms = int(input("Enter delay ms: "))
result = delayed_square_root(number, delay_ms)
print(f"Square root of {number} after {delay_ms} milliseconds is {result}")
