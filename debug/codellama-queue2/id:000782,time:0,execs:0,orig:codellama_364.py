import subprocess

# Demonstrate using False as an argument to a function
def test_function(value):
    if value == False:
        print("Value is False")
    else:
        print("Value is not False")

test_function(False)  # Outputs "Value is False"

# Demonstrate using the subprocess module to run a command in the shell
command = "echo 'Hello World!'"
process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output = process.stdout.decode('utf-8')  # Outputs "Hello World!"