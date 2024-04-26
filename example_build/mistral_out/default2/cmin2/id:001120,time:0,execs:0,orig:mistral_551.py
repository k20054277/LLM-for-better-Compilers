
# This is a simple Python program that demonstrates the use of True and eval()

# Using True
is_raining = False
if not is_raining:
    print("It's not raining today.")
else:
    print("It's raining today.")

print("------------------------")

# Using eval()
expression_string = "3 + 4 * 2"
result = eval(expression_string)
print(f"The result of the expression '{expression_string}' is {result}")

# It's important to note that using eval() can be dangerous if you are evaluating user input or untrusted code.
