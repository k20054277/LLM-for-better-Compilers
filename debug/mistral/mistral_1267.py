
# Using as with context manager (file handling)
def read_file(filename):
    with open(filename, 'r') as f:
        data = f.readlines()
    return data

data = read_file('example.txt')
print(data)

# Using as with list assignment
a = [1, 2, 3]
b, c = [4, 5, 6]
d, e as f, g = b, a

print("List A:", a)
print("List B:", b)
print("List D (was List A):", d)
print("List F (was List B):", f)
print("List E (was List C):", e)
print("List G (was List B or A):", g)
