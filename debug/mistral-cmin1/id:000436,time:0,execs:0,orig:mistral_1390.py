
import subprocess

def get_python_version():
    result = subprocess.run(["python", "--version"], capture_output=True, text=True)
    return result.stdout.split(" ")[2].split(".")[0:2]  # Extract major and minor version

# Check Python version
python_version = get_python_version()
minor_version = int(python_version[1]) if len(python_version) > 1 else 0
assert minor_version >= 8, "Python version should be 3.8 or above."

# Arithmetic operation assertion
def add(x, y):
    return x + y

assert add(1, 2) == 3, "The function 'add' is not working correctly."
