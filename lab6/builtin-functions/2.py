def count_case_letters(s):
    upper_case = sum(1 for char in s if char.isupper())
    lower_case = sum(1 for char in s if char.islower())
    return upper_case, lower_case

input_string = "Hello World"
upper, lower = count_case_letters(input_string)
print(f"Uppercase letters: {upper}, Lowercase letters: {lower}")
