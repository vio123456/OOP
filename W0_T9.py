# read_file.py

filename = input("Insert filename to read: ")

try:
    with open(filename, 'r') as file:
        print(f"#### {filename} content ####")
        print(file.read())
        print(f"#### {filename} content ####")
except FileNotFoundError:
    print(f"File '{filename}' not found.")
