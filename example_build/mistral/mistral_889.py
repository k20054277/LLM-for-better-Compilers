
import os

# Check if a file exists and is a regular file (not a directory)
file_path = "/path/to/your/file.txt"
if os.path.isfile(file_path) and os.path.isdir(file_path) is False:
    print("File exists and is a regular file.")
else:
    print("File does not exist or is a directory.")

# Use 'and' as a logical operator in a different context (comparing two conditions)
if 5 > 3 and "apple" in ["apple", "banana"]:
    print("Condition 1 is True and Condition 2 is True.")
else:
    print("At least one of the conditions is False.")
