# demonstrate the use of False and is

print(False)  # prints "False"
print(True)   # prints "True"
print(5 > 6)  # prints "False"
print(5 < 6)  # prints "True"

x = 10
y = 20

if x is y:
    print("x and y are the same object")
else:
    print("x and y are different objects")