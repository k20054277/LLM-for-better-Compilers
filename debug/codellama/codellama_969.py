import subprocess

# Create a list of commands to run
commands = ["echo 'Hello, World!'", "ls -l"]

# Use the shell to execute each command and store the output
outputs = []
for command in commands:
    outputs.append(subprocess.check_output(command, shell=True))

# Print the output of each command
print("Command 1:", outputs[0].decode('utf-8'))
print("Command 2:", outputs[1].decode('utf-8'))