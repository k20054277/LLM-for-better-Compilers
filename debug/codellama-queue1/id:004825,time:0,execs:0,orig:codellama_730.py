# Asking for input from the user
name = input("Please enter your name: ")

# If the user inputs a string that is "John", then print out a message indicating that the user has entered the correct name.
if name == "John":
    print("Hello, " + name + ". You have entered the correct name.")
else:
    # If the user did not enter the correct name, then prompt them to try again.
    print("Sorry, " + name + ". Try again!")