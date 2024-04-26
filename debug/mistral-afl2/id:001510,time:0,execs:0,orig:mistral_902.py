
import os
import subprocess

# Define the directory path
directory_path = "/path/to/your/directory"

# Check if directory exists
if os.path.isdir(directory_path):
    print(f"Directory '{directory_path}' exists.")
else:
    print(f"Directory '{directory_path}' does not exist.")
    
# If directory exists, execute a command using subprocess
if os.path.isdir(directory_path):
    # Define the command to run (in this example, we will execute 'ls' command)
    command = "ls"

    # Execute the command in the directory using subprocess
    process = subprocess.Popen(command, shell=True, cwd=directory_path)

    # Get the output of the command and print it
    output, error = process.communicate()
    if error is not None:
        print("Error occurred while executing command:", error.decode())
    else:
        print("Output of command 'ls' in directory '{directory_path}':")
        print(output.decode())
else:
    print("Directory does not exist, so no command execution.")
