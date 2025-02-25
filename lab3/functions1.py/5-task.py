import itertools

def print_permutations(input_string):
    permutations = itertools.permutations(input_string)
    for perm in permutations:
        print(''.join(perm))

user_input = input("Enter a string: ")
print_permutations(user_input)
