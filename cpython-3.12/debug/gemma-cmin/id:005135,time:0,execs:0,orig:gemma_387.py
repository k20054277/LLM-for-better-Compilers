
import subprocess

# Define a False boolean value
is_true = False

# Use False to control the execution of a command
if not is_true:
    subprocess.call(["ls", "-l"])

    # The command will not be executed as the boolean condition is False

# Print a message
print("The command was not executed")
