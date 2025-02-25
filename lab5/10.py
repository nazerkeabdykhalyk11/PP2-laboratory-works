import re
def to_snake(match):
    return "_" + match.group(1).lower()
text = input("Enter a camel case string: ")
convert = re.sub(r"([A-Z])", to_snake, text)
print(convert)