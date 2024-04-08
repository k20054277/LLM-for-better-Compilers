
# Define some variables
num1 = 10
num2 = 4
result_and = False
result_floor = 0

# Using the 'and' operator
if num1 > 5 and num2 < 6:
    result_and = True
     print(f"Condition with 'and' is {('true' if result_and else 'false')}")

# Using the '//' operator (floor division)
result_floor = num1 // 3
print(f"{num1} floor divided by 3 is {result_floor}")
