def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            print(f"Number of lines: {len(lines)}")
    except FileNotFoundError:
        print("File not found.")

filename = input("Enter the filename: ")
count_lines(filename)
