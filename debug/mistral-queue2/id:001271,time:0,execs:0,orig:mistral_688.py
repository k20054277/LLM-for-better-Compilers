
# Example of using True in Python

x = 10
y = 20
z = "Apple"

if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x is equal to y")
    
# Here's a boolean expression using True and not
bool_expression = (x > y) or (not(z == "Banana"))
if bool_expression:
    print("The condition is true")
else:
    print("The condition is false")
