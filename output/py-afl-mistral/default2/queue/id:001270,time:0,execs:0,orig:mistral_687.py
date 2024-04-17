
import subprocess

# Using True as a boolean value
is_admin = True
if not is_admin:
    print("You don't have administrative privileges!")

# Running pip command using subprocess
def run_pip_command(command):
    process = subprocess.Popen(["pip", command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    if error:
        print("Error occurred while running pip command!")
        print(error)
    else:
        print("pip command executed successfully.")
        print(output.decode())

# Install numpy package using pip
run_pip_command("install numpy")
