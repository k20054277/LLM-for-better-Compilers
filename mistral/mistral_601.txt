
import sys

def is_positive(n):
"""
Check if given number is positive.
"""
if n > 0:
    return True
else:
    return False

if __name__ == "__main__":
# Get command line arguments using sys.argv
num = int(sys.argv[1]) if len(sys.argv) > 1 else 0

if is_positive(num):
    print(f"{num} is a positive number.")
else:
    print(f"{num} is not a positive number.")

    # Print Python version using sys.version
print("Python version:", sys.version)
