
# Boolean values: True and False
bool_true = True
bool_false = False

print("Boolean value: True is ", bool_true)
print("Boolean value: False is ", bool_false)

# Comparison with False
num1 = 5
num2 = 10

if num1 < num2:
    print(f"{num1} is less than {num2}")
else:
    print(f"{num1} is greater than or equal to {num2}")

# Logical NOT (invert) operation with False
bool_not = not bool_false
print("Logical NOT of False is:", bool_not)

# Comparison with zero using False
num = 0
if num:
    print(f"{num} is not equal to zero")
else:
    print(f"{num} is equal to zero")
