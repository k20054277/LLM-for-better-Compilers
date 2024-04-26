
import subprocess

# This assignment sets a variable named 'status' to the True boolean value
status = True

print("Status before command execution: {}".format(status))

# Use the subprocess module to run the 'dir' command in the current system shell
result = subprocess.run(["dir"], capture_output=True, text=True)

# Assign the output of the command to a variable named 'output'
output = result.stdout

# Print the output of the command and change the value of the 'status' variable based on the exit code of the command
print("\nOutput of the command: {}".format(output))
if result.returncode == 0:
    status = True
else:
    status = False

print("Status after command execution: {}".format(status))
