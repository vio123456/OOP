# Python program to check if a string is memorable based on its length
print("Per Miller's Law, humans can retain ~7 items in short-term memory.")
# Get the string input from the user
input_string = input("Insert memorable string: ")

# Check if the string is less than 7 characters long
if len(input_string) < 7:
    print("This string will be easy to remember.")
else:
    print("This string will be hard to remember.")