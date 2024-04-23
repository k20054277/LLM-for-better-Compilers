# Example using "as"
try:
    with open("file.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found!")

# Example using "else"
for i in range(5):
    if i == 3:
        break
else:
    print("Loop finished normally.")