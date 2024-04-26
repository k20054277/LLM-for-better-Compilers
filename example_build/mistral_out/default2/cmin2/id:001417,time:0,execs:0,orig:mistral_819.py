
# Variables definition
num = 0
limit = 10

# Checking if a number is greater than zero and less than a limit using 'and'
print("Using 'and':")

while num != limit:
    if num > 0 and num < limit:
        print(f"Number: {num}, It should be increased.")
        num += 1
    else:
        print(f"Number: {num}, It's either greater than or equal to the limit.")
        break

print(f"\nThe number is now: {num} and it's equal to the limit.")

# Using 'and' in a while condition
print("Using 'and' in a while condition:")

num = 0

while num != limit and num >= 0:
    print(f"Number: {num}")
    if num == limit:
        break
    num += 1
