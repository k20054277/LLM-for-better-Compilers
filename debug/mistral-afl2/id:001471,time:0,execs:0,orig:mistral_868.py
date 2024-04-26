
# Set file path and access conditions
file_path = "example.txt"
readable = True
writable = False

# Check if the file exists and is readable
if os.path.exists(file_path) and os.access(file_path, os.R_OK):
    # Open the file in read-only mode
    with open(file_path, 'r') as file:
        content = file.read()
        print("File contents:", content)
else:
    print("Error: File does not exist or is not readable")

# If the file is writable, you can also write to it
if writable and os.access(file_path, os.W_OK):
    with open(file_path, 'w') as file:
        new_content = "This is new content."
        file.write(new_content)
        print("File has been updated with new content.")
