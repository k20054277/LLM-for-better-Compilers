
# Define two boolean variables
boolean1 = False
boolean2 = True

# Test boolean variables using 'and' operator
result = boolean1 and boolean2

# Print the result
if result:
    print("Both boolean values are true")
else:
    if not boolean1:
        print("First boolean value is false")
    else:
        print("First boolean value is true, but second boolean value is false or they both are false")

    if not boolean2:
        print("Second boolean value is false")
