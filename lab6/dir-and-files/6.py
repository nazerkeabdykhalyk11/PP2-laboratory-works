import string

def generate_files():
    for letter in string.ascii_uppercase:  # A-Z
        filename = f"{letter}.txt"
        with open(filename, 'w') as file:
            file.write(f"This is file {filename}\n")
    print("26 text files created.")

generate_files()
