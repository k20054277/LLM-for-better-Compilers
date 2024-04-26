
# This Python program demonstrates the use of and and str

# Define a function to demonstrate the use of and and str
def demonstrate_and_str(name, age):
    # Use the and operator to check if name is not None and age is greater than 18
    if name and age > 18:
        # Convert the age to a string and concatenate it with the name
        message = f"Hello, {name}. You are {age} years old."
        # Print the message
        print(message)

# Get the name and age from the user
name = input("What is your name? ")
age = int(input("How old are you? "))

# Call the function to demonstrate the use of and and str
demonstrate_and_str(name, age)
