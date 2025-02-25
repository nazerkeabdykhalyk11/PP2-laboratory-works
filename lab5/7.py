import re
def to_upper(match):
    return match.group(1).upper()
text = input("Enter a snake case string: ")
convert = re.sub(r"_([a-z])", to_upper, text)
print(convert)