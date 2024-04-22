
import pkg_resources

# Define a boolean variable
is_active = False

# Print the value of the boolean variable
print(is_active)

# Check if the package "my_package" is installed
if pkg_resources.is_package("my_package"):
    # Print the package version
    print(pkg_resources.get_version("my_package"))
else:
    # Print an error message
    print("Error: Package not installed")
