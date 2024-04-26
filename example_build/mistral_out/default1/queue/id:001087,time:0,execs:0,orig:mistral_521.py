
# Demonstrating True as a Boolean Value
x = 10
y = 20
z = x

print("Condition 1:")
if x > 5:
    print(f"{x} is greater than 5. So, the condition is true.")
else:
    print(f"{x} is less than or equal to 5. So, the condition is false.")
print("But, {0} is a truth value and it evaluates as true.".format(True))

# Demonstrating is operator
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print("Condition 2:")
if id(a) == id(b):
    print("a and b are the same object in memory. So, this condition is true.")
elif id(a) is id(c):
    print("a and c are the same object in memory. So, this condition is true.")
else:
    print("None of a, b or c are the same objects in memory. So, these conditions are false.")
