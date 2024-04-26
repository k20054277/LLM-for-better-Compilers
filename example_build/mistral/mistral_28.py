
# Define some variables
variable1 = False
variable2 = True
condition1 = variable1 or variable2

print("Variable 1 is:", variable1)
print("Variable 2 is:", variable2)

print("\nUsing 'or' operator:")
print("If variable 1 is True or variable 2 is True, then the condition is True.")
print("So in our case, since variable 1 is False and variable 2 is True,")
print("the condition will be:", condition1)
print("which is:", condition1, "\n")

# Let's change the value of variable1 and check the condition again
variable1 = True
condition1 = variable1 or variable2

print("\nAfter changing variable 1 to True:")
print("Variable 1 is now:", variable1)
print("Variable 2 is:", variable2)
print("So the new condition is:", condition1, "\n")
