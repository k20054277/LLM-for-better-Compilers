
import subprocess

# Define a True statement
is_true = True

# Use True to control a subprocess
subprocess.run(["echo", "Hello, world!"], True)

# Print the output of the subprocess
print(subprocess.stdout.decode())

# Output: Hello, world!
