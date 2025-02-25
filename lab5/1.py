import re
text = str(input("Enter string: "))
match = re.fullmatch(r'ab*',text)
if match:
    print("Yes, it matches")
else:
    print("No, it doesn't match")