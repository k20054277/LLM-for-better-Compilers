
import subprocess

# This is a boolean value, False represents false conditions
is_admin = False

if not is_admin:
    print("You don't have admin privileges.")
    
    # Run a harmless shell command that doesn't require admin privileges
    result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
    print("\nListing directory contents:")
    print(result.stdout)
else:
    print("You have admin privileges.")
    
    # Run a shell command that requires admin privileges (e.g., formatting a USB drive)
    command = "sudo format /dev/sdb1"  # replace with the actual command you need
    result = subprocess.run(command, capture_output=True, text=True, check=True)  # use 'check=False' if you want to ignore errors
    print("\nCommand output:")
    print(result.stdout)
