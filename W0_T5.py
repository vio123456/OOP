# Python program to prompt the user to add numbers using a while-loop

current_value = 0.0  # Initialize the current value to 0.0

# Start the while-loop, which will run until the user enters an empty string
while True:
    
    # Display the current value
    print(f"Current value {current_value:.1f}")
    
    # Prompt the user to add a number, or enter an empty string to stop
    user_input = input("Add number(empty stops): ")
    if user_input == "":
        print(f"Final value {current_value:.1f}")
        break
    else:
        current_value=current_value+float(user_input)
    

   

