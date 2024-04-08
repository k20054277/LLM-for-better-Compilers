
import subprocess

# Define a function that checks if a file exists and returns True or False
def file_exists(file_path):
    return subprocess.call([sys.executable, '-c', '"import os, print(os.path.isfile(%r))"' % file_path], shell=True) == 0

# Check if a file exists and print a message accordingly
if file_exists("/path/to/your/file.txt"):
    print("File exists!")
else:
    print("File does not exist.")

# Use shell to run a command and store the output in a variable
result = subprocess.run(["ls", "-l"], capture_output=True, text=True, shell=True)
print(f"Output of 'ls -l' command: {result.stdout}")
