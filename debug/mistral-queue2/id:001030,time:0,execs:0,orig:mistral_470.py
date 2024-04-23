
# Define some variables
var1 = 42
var2 = "forty-two"
var3 = None

# Assigning None to a variable
print("Assigning None to a variable:")
var4 = None
print("Type of var4: ", type(var4))

# Checking for None
print("\nChecking if a variable is None:")
if var3 is None:
    print("var3 is None.")
else:
    print("var3 is not None.")

# Comparing with None using 'is' keyword
print("\nComparing with None using 'is':")
if var4 is None:
    print("var4 is None.")
else:
    print("var4 is not None and has value:", var4)

# Comparing with None using '==' operator
print("\nComparing with None using '==' operator:")
if var4 == None:
    print("None and None are equal.")
elif var4 is None:
    print("Variable is None, but comparison failed.")
else:
    print("var4 has a value:", var4)

# Assigning values and checking for equality using '==' operator
print("\nAssigning values and checking for equality using '==' operator:")
var5 = 42
if var1 == var5:
    print("var1 and var5 are equal.")
else:
    print("var1 and var5 are not equal.")
