
# This Python program demonstrates the use of the and and batch commands

# Import the necessary libraries
import os

# Define a list of files to be processed
files = ["file1.txt", "file2.txt", "file3.txt"]

# Use the and command to execute multiple commands on the files
for file in files:
    os.system("and cat " + file + " && echo " + file)

# Use the batch command to execute a command on a group of files
os.system("batch echo %~dp0\\*")
