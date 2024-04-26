
import pip

# Print the version of pip
print("Pip version:", pip.__version__)

# Check if a package named "my_package" is installed
if not pip.find("my_package"):
    # If the package is not installed, install it
    pip.install("my_package")

# Import the package
import my_package

# Print a message from the package
print("Hello, from my_package!")
