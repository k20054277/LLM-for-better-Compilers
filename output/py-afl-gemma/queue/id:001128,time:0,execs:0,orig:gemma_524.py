
# Import the necessary library
import pkg_resources

# Define a function that checks if a package is installed
def is_package_installed(package_name):
    # Check if the package is installed
    if pkg_resources.is_package(package_name):
        return True
    else:
        return False

# Check if the package "my_package" is installed
if is_package_installed("my_package"):
    print("Package 'my_package' is installed.")
else:
    print("Package 'my_package' is not installed.")

# Install the package if it is not installed
if not is_package_installed("my_package"):
    pkg_resources.install("my_package")
    print("Package 'my_package' has been installed.")
