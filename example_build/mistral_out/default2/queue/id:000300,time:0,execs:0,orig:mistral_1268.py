
# Assign the standard input stream to a variable named 'file' using as keyword
with open('example.txt', mode='r') as file:
    content = file.read()
    
# Now, you can use the new name 'content' to access the string read from the file
print(content)
