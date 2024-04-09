
# This Python program demonstrates the use of and and as

# Define a function called greet
def greet(name, language):
    # Use the and operator to check if the language is English or Spanish
    if language == "English" or language == "Spanish":
        # Use the as operator to assign the translated message to the message variable
        message = f"Hello, {name}. Welcome to the {language}!"
    else:
        # Otherwise, use a different message
        message = f"Hello, {name}. Welcome to the default language!"

    # Print the message
    print(message)

# Get the name and language of the user
name = input("What is your name? ")
language = input("What is your language? ")

# Call the greet function
greet(name, language)
