
import subprocess

# Define the command you want to run as a list containing the executable and arguments
command = ["ls", "-la"]

# Run the command using subprocess.run()
output, error = subprocess.run(command, capture_output=True, text=True)

if error:
    print("Error running command:", error)
else:
    # Print the output
    print("Output:\n", output)
