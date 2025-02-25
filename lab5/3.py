import re
text = str(input("Enter a string joined with a underscore: "))
match = re.findall(r'[a-z]+_[a-z]+', text)
if match:
        print(f'Sequences found: {match}')
else:
        print('No sequences found.')