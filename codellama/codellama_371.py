with open("example.txt", "w") as file:
    file.write("This is a test.")

# Use False to check if the file exists
if not os.path.exists("example.txt"):
    print("The file does not exist.")
else:
    print("The file exists.")

# Use context manager to open the file and read its contents
with open("example.txt", "r") as file:
    contents = file.read()
print(contents)