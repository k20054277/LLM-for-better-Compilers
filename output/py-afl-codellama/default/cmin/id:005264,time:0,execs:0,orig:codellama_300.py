import package_manager

def main():
    # Check if a package is installed
    if package_manager.is_installed("my-package"):
        print("The 'my-package' package is installed.")
    else:
        print("The 'my-package' package is not installed.")

# Use the `False` keyword to indicate that a package is not installed
def check_package(package_name):
    if package_manager.is_installed(package_name):
        return True
    else:
        return False

# Check if a package is installed and print a message if it is
if check_package("my-package"):
    print("The 'my-package' package is installed.")
else:
    print("The 'my-package' package is not installed.")