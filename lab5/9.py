import re
def to_split(match):
    return " " + match.group(1)
text = input("Enter string with uppercase letters: ")
result = re.sub(r"([A-Z])", to_split, text)
print(result)