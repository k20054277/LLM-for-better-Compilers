
# Assigning a file object to a variable 'file' using 'as' keyword
with open('example.txt') as file:
  data = file.readline()
  print(data)

# Unpacking tuples or lists with 'as'
a, b = (1, 2)
x, y = (3, 4)
a, b = a, b as x, y
print("a =", a, ", b =", b)
print("x =", x, ", y =", y)
