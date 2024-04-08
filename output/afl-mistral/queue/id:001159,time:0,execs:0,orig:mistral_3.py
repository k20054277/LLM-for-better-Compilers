
# An assignment where x is set to 10 and y is set to 5.
x = 10
y = 5

# Comparison using < (less than) operator.
if x < y:
    print("x is less than y") # This statement will not be executed because False condition prevents the execution of statements following it in the code block.
    false_value = True # This line would set false_value to True if the if statement did not have a False condition.

# Comparison using > (greater than) operator.
if x > y:
    print("x is greater than y") # This statement will be executed because the condition is True.

# Direct assignment of Boolean values.
false_value = False
true_value = True

print(f"False value is: {false_value}") # Output: False value is: False
print(f"True value is: {true_value}")  # Output: True value is: True
