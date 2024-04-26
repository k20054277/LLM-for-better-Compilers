
# Open a file using 'with' statement which acts as a context manager
with open('example.txt', 'r') as f:  # 'r' stands for read mode
    # Read the entire content of the file into a variable
    data = f.read()

# Now print the contents and perform some other operations if needed
print(f"The file 'example.txt' contains: {len(data)} characters.")
print(data)
