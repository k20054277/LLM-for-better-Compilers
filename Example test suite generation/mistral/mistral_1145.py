
import subprocess

# Using subprocess.run with a context manager for handling output as text
def run_command(command):
    process = subprocess.run(command, shell=True, stdout=subprocess.TEXT, stderr=subprocess.STDOErr)
    return process.stdout

if __name__ == "__main__":
    command = "ls -lah"
    output = run_command(command)
    print("Output of the command:\n{}".format(output))

# Using as and context manager to handle output as bytes
def run_command_bytes(command):
    with subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as process:
        output, error = process.communicate()
    return (output, error)

if __name__ == "__main__":
    command = "ls -lah"
    output, error = run_command_bytes(command)
    print("Output of the command as bytes:\n{}".format(output))
    if error:
        print("Error from command execution:\n{}".format(error))
