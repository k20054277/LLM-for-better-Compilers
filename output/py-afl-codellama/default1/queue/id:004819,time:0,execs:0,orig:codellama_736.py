# Example 1: Using True and False to control flow
if True:
    print("This will always be executed")
else:
    print("This will never be executed")

# Example 2: Using a conditional statement with True and False
x = 5
if x > 10:
    print("x is greater than 10")
elif x < 10:
    print("x is less than 10")
else:
    print("x is equal to 10")

# Example 3: Using True and False in a loop
for i in range(5):
    if i == 3:
        break
    else:
        print(i)