
import subprocess
import sys

# Define the command to be executed
command = ["ls", "-l"]

# Execute the command using subprocess.Popen
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Capture the output of the command
output, error = process.communicate()

# Print the output
print(output.decode("utf-8"))

# Check if there was an error
if error:
    print(error.decode("utf-8"))

# Close the process
process.close()
