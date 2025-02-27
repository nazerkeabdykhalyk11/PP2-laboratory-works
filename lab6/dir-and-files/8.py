import os

def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print(f"File {path} deleted.")
        else:
            print("File is not writable, cannot delete.")
    else:
        print("File does not exist.")

file_path = input("Enter file path to delete: ")
delete_file(file_path)
