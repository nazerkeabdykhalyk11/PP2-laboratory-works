def copy_file(source, destination):
    try:
        with open(source, 'r') as src, open(destination, 'w') as dest:
            dest.write(src.read())
        print(f"Copied contents from {source} to {destination}")
    except FileNotFoundError:
        print("Source file not found.")

source_file = input("Enter source file: ")
destination_file = input("Enter destination file: ")
copy_file(source_file, destination_file)
