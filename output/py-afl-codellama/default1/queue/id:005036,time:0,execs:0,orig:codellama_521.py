# Using None as a default value for a variable
x = None
if x is None:
    print("The variable x has no value.")
else:
    print("The variable x has the value", x)

# Using None as a condition in an if statement
if None:
    print("This code will never execute because None is Falsey.")
else:
    print("This code will execute because None is Falsey.")

# Using None in a loop
for i in range(5):
    if i == 3:
        break
    print(i)
print("Loop finished!")