numbers_input = input("Enter numbers separated by space: ")  
my_tuple = tuple(map(int, numbers_input.split()))  

print(all(my_tuple))
