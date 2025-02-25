import re
text = str(input("Enter a string: "))
match = re.search(r'a.*b',text)
if match:
    print("Yes, it matches")
else:
    print("No, it doesn't match")