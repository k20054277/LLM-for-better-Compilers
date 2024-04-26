# Using False and not with if statements
x = 10
if x > 20:
    print("x is greater than 20")
elif x < 20:
    print("x is less than 20")
else:
    print("x is equal to 20")

# Using False and not with conditional expressions
y = 15
if y > 20:
    z = True
else:
    z = False
print(z)

# Using False and not with loops
for i in range(1, 11):
    if i % 2 == 0:
        print(i)