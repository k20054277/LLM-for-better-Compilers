# Demonstrate the use of True and exec

# Define a function that takes a boolean argument and returns its negation
def negate(x):
    return not x

# Execute the negate function with True as an argument, which should result in False
exec("result = negate(True)")
print(result)  # Should print False

# Execute the negate function with False as an argument, which should result in True
exec("result = negate(False)")
print(result)  # Should print True