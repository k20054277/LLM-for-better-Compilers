
# This Python program demonstrates the use of the as and shell commands

# Define a variable and assign it to a shell object
shell = os.popen("bash")

# Use the shell object to execute commands
shell.write("echo Hello, world!")

# Read the output of the shell command
output = shell.read()

# Print the output
print(output)

# Close the shell object
shell.close()
