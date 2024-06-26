
import subprocess

# Using None
# In Python, None is a special value used to represent the absence of a value or a variable which has not been initialized.

# Example 1: Assigning None to a variable
none_value = None
print("None value type:", type(none_value))
if none_value is None:
    print("None value is set.")

# Example 2: Using None as an argument or return value from a function
def greet(name=None):
    if name is None:
        print("Hello, World!")
    else:
        print(f"Hello, {name}!")

greet() # Hello, World!
greet("John") # Hello, John!

# Interacting with the Shell using subprocess
def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    if error:
        print("Error occurred:", error.decode())
    else:
        print("Output of command '{}': {}".format(command, output.decode()))

# Example 1: Running a command and capturing its output
run_command("echo Hello, World!")

# Example 2: Running a command with arguments
run_command("ls -l /usr/bin/")
