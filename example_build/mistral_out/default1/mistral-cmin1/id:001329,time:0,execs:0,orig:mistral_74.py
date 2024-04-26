
def print_if_false(condition):
    if condition is False:
        print("The condition is false")

# Define some variables
name = "Alice"
age = 25
is_student = False

print("Before function call:")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Is student: {is_student}")

# Call the print_if_false function with the is_student variable as an argument
print("Function call:")
print_if_false(is_student)

print("After function call:")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Is student: {is_student}")

# Print the locals dictionary to check its contents
print("Locals dictionary:")
locals_dict = locals()
for key, value in locals_dict.items():
    print(f"{key}: {value}")
