
# This Python program demonstrates the use of True and shell

# Define a boolean variable
is_active = True

# Print a message based on the value of the variable
if is_active:
    print("The system is active")

# Execute a shell command using the shell module
import shell
shell.write("ls -l")

# Print the output of the shell command
print(shell.read())
