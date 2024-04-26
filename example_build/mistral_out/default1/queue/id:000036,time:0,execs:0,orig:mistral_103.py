
import os

# Set a variable to False
is_morning = False

print("Is it morning?", is_morning)

# Use os.path.exists() to check if a file exists and print a message accordingly
file_path = "example.txt"
if not os.path.exists(file_path):
    print(f"The file '{file_path}' does not exist.")
else:
    print(f"The file '{file_path}' exists.")

# Use an if statement with False to check if a condition is not met
if not is_morning:
    print("It's not morning yet. Please wait a bit longer.")
else:
    print("Good morning! Let's start the day.")
