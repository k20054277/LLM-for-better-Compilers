
# This script checks if a file exists and prints a message accordingly

# Define the file name
file_name = "example.txt"

# Check if the file exists and open it if it does
if open(file_name, mode="r"):
    print("File exists and can be opened.")
else:
    print("File does not exist or cannot be opened.")

# Perform some true/false statements as examples
is_even = 6 % 2 == 0
print(f"Is {6} an even number? -> {is_even}")

is_odd = 7 % 2 != 0
print(f"Is {7} an odd number? -> {is_odd}")
