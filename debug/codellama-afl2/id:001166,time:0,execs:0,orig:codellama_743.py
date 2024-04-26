# Print "Hello, World!" if the user's name is "Alice"
name = input("What is your name? ")
if name == "Alice":
    print("Hello, Alice!")
else:
    print("Hello, {}.".format(name))