# using as
x = 10
y = x as float
print(y) # prints 10.0

# using with
with open("example.txt", "r") as file:
    print(file.read())