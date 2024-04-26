
import os

# Command 1: Check if directory exists and create it if not
command_1 = "mkdir -p my_directory &&"

# Command 2: Change to the created directory
command_2 = "cd my_directory"

try:
    # Execute both commands using os.system() with '&&' operator
    os.system(command_1 + command_2)
except OSError as error:
    print("Error creating directory and/or changing to it:", error)
