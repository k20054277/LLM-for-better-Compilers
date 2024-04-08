
# Define a variable with an initial value of True
is_student = True

# Perform some checks and update the variable based on conditions
if 10 > 5:
    print("Five is less than ten")
else:
    print("Ten is not less than five")

# Use the boolean value False in a comparison
if is_student and not (age < 18):
    print("You can vote")
else:
    print("You cannot vote")

# Update the variable based on another condition
is_student = not is_student
print("I am now a non-student:", is_student)
