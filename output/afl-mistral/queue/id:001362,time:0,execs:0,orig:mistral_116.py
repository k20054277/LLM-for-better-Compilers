
import subprocess

# Setting up the command to be executed (a non-existent command for demonstration)
command = "non_existent_command"

try:
    # Using subprocess.check_call() to execute the command, with stdout and stderr redirected to a pipe
    result = subprocess.check_call(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
except subprocess.CalledProcessError as e:
    # If an error occurs (i.e., the command is non-existent), the program will print an error message and exit with False status
    print(f"An error occurred while executing {command}:")
    print(f"Error output: {e.output.decode('utf-8')}")
    print(f"Exit code: {e.returncode}")
    exit(False)

# If the command execution was successful, the program will continue with further instructions (which are not included in this example for simplicity)
print("Command execution was successful!")
