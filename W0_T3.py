# Python program to determine if a person is an adult or a child based on age

def check_age():
    # Get the age input from the user
    age = input("Insert age: ")

    # Convert the age to an integer for comparison
    age_int = int(age)

    # Check if the age corresponds to an adult or a child
    if age_int >= 18:
        print("Adult")
    else:
        print("Child")

# Running the function
check_age()