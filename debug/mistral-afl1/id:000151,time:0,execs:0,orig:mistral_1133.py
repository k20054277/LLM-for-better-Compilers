
import sys

# Using sys.stdin, sys.stdout for standard input and output
print("Enter your name:")
name = input("> ")  # Using input as default function for getting user input

sys.stdout.write("Hello, ")
sys.stdout.write(name)
sys.stdout.write("! You have invoked this program.\n")

# Using 'as' for assignment with alias
try:
    file = open('example.txt', 'r') as f_handle
except FileNotFoundError:
    print("The file does not exist.")
else:
    content = f_handle.read(10)
    print(f"First 10 characters of the file: {content}")
finally:
    if file is not None:
        file.close()
