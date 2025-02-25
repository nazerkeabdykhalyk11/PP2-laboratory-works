import re
text = input("Enter a string: ")
match = re.fullmatch(r'ab{2,3}', text)
if match:
    print("Yes, it matches")
else:
    print("No, it doesn't match")