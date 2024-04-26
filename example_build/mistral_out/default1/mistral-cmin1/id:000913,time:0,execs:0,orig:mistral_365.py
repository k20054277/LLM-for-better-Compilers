
import subprocess

# Attempt to run a nonexistent command using subprocess.Popen
try:
    result = subprocess.run(["nonexistent_command"], capture_output=True, text=True)
except FileNotFoundError as error:
    print("Error: The specified command is not found.")
    result = None

if result is not None:
    # If the command execution was successful, print its output
    print("Command Output:")
    print(result.stdout)
else:
    print("Command Execution failed or the command did not exist.")
