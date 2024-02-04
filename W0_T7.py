try:
    # Code that could potentially cause an error goes here.
    number = float(input("Insert number: "))
    print(f"Inserted value is '{number}'")
except ValueError:
    # This block handles the error if it occurs.
    print("Oops! That wasn't valid number.")
