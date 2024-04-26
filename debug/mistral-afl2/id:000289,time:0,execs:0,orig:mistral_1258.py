
# Define two numbers with initial values
num1 = 10
num2 = 5

# Division using standard division operator (/)
result = num1 / num2
print(f"Result of standard division: {result}")

# Division assignment using /= operator
num1 /= num2
print(f"Num1 after division assignment: {num1}")

# Multiplication and assignment using as operator
factor = 3
num1 *= factor as new_num
print(f"Num1 after multiplication assignment using 'as': {num1} (previously was {num1} and now is equal to {new_num})")
