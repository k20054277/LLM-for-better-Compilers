
import sys

# Print the name of the current module
print(sys.modules[__name__])

# Print the version of Python being used
print(sys.version)

# Check if the Python version is greater than 3.5
if sys.version_info[0] >= 3 and sys.version_info[1] >= 5:
  print("Python version is greater than 3.5")

# Exit the program
sys.exit()
