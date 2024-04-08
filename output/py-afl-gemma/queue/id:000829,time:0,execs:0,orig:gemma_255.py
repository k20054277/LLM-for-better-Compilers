
import subprocess

# Define a command to execute
command = ["ls", "-l"]

# Execute the command using subprocess
subprocess.call(command)

# Print the output of the command
print(subprocess.check_output(command).decode("utf-8"))
