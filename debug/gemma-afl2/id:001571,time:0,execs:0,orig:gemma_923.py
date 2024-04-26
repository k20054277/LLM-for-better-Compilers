
import os

# Check if the operating system is Windows
if os.name == "nt":
    print("You are using Windows")

# Check if the operating system is Mac OS
elif os.name == "darwin":
    print("You are using Mac OS")

# Check if the operating system is Linux
elif os.name == "posix":
    print("You are using Linux")

# Print the operating system name
print("Your operating system name is:", os.name)
