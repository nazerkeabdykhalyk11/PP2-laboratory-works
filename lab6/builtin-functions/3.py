def is_palindrome(s):
    return s == ''.join(reversed(s))

input_string = str(input("Enter sentence: "))
if is_palindrome(input_string):
    print(f"{input_string} is a palindrome")
else:
    print(f"{input_string} is not a palindrome")
