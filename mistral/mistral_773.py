
# Define some boolean variables
variable1 = False
variable2 = True

print("Variable 1 is:", variable1)
print("Variable 2 is:", variable2)

# Perform bitwise OR operation on two boolean values using the '|' operator
result = variable1 | variable2

print("\nThe result of (variable1 | variable2) is:")
print(result)

# Interpreting the result with the help of truth table
print("\nTruth Table:\n"
      "|------|-------|--------------|\n"
      "|  A   |  B   |   A | B    | A | B | A OR B |\n"
      "|------|-------|--------------|-------|-----|----|------------------|\n"
      "| False| False |False       | False | 0  | 0  |     False        |\n"
      "| False|  True |False       |  True | 0  | 1  |       True        |\n"
      "|  True| False |False       | False |1  | 0  |       True        |\n"
      "|  True|  True |True       |  True |1  | 1  |       True        |\n")
