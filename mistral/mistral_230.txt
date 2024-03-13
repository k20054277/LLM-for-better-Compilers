
# Define two variables with initial values
x = 10
y = 5

# Check if x is greater than y using a boolean expression
if x > y:
    print("x is greater than y")
else:
    print("x is not greater than y")

# Use the false boolean value in an assignment statement
is_even = False
num = 3
if num % 2 == 0:
    is_even = True

print(f"Is {num} even? - Answer: {is_even}")

# Use the divide-and-assign operator to divide x by y and assign quotient to x
x //= y
print(f"After x = x // y: x is now {x}")
