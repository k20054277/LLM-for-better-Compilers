
# Demonstrating False as a boolean value

x = 5
y = 10
z = "not a number"

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")

# false statement
if not(x < y):
    print("x is not less than y (which is False)")
