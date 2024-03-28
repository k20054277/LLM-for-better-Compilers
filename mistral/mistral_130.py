
# Example of using False in Python
x = 10
if x < 5:
    print("x is less than 5")
else:
    print("x is greater than or equal to 5")
    x += 1 # This line will not be executed because the if statement is false
print(x) # Output: 10
