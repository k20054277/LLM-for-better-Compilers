
# This Python program demonstrates the use of as and exec

# Define a function to execute a string as a Python command
def execute_command(command):
    # Use the as keyword to bind the output of the command to the variable "result"
    result = exec(command)

    # Return the result of the command
    return result

# Get the command to execute from the user
command = input("Enter a Python command: ")

# Execute the command and print the result
result = execute_command(command)

# Print the result
print("The result of the command is:", result)
