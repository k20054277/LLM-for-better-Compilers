
def get_name():
    name = input("Please enter your name: ")
    if not name:
        name = None
        print("No name entered, setting name to None.")
    return name

# Get user's name and print a greeting
name = get_name()
if name is not None:
    print(f"Hello, {name}!")
else:
    print("No name provided.")
