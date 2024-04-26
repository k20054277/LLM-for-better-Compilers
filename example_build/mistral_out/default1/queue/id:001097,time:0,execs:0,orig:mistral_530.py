
# Initialize a variable with a value that can be changed to False
is_alive = True

print("This program is about a life cycle.")

while is_alive:
    # Ask the user if they want to continue the game (or in this case, the program)
    user_answer = input("Do you want to continue? (y/n): ")

    # Convert the user's answer to lowercase and check for 'y' or 'n'
    if user_answer.lower() == 'y':
        print("Great! Let's continue.")
    elif user_answer.lower() == 'n':
        print("Okay, exiting the program...")
        is_alive = False
    else:
        print("Invalid input. Please enter y or n.")
