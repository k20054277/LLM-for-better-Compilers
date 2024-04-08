import subprocess

# None is used to represent the absence of a value
none_example = None
print(none_example)  # Output: None

# subprocess is used to run external commands
result = subprocess.run(['ls', '-l'])
print(result)  # Output: <subprocess.CompletedProcess at 0x109a35748>