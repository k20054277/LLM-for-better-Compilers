# Print "Hello, World!" if the user inputs "yes" or "y", otherwise print "Goodbye."
user_input = input("Enter yes or y to say hello: ")
if user_input.lower() == "yes" or user_input.lower() == "y":
    print("Hello, World!")
else:
    print("Goodbye.")