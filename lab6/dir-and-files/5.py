def write_list_to_file(filename, data_list):
    with open(filename, 'w') as file:
        for item in data_list:
            file.write(str(item) + '\n')
    print(f"List written to {filename}")

my_list = ["Python", "is", "awesome!"]
filename = "output.txt"
write_list_to_file(filename, my_list)
