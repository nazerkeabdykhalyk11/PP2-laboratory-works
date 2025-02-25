import re
text = input("Enter some string: ")
print(re.sub(r"[ ,.]", ":", text))