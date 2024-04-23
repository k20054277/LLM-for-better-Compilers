
# Import the shell module
import shell

# Define a False boolean value
false = False

# Print a message if the boolean value is False
if false:
    print("The boolean value is True")

# Use the shell module to execute a command
shell.exec("ls -l")

# Print the output of the command
print(shell.output)
