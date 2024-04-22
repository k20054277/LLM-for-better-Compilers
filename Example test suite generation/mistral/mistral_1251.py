
# Assignment using 'as'
try:
    file = open("example.txt", "r") as file_handle
except FileNotFoundError:
    print("File not found!")
else:
    content = file_handle.read()
    print(f"Content of the file:\n{content}\n")
    file_handle.close()

# Comparison using '!='
x = 10
y = "twenty"

if x != y:
    print("x and y are not equal! (x is an integer, y is a string)")
