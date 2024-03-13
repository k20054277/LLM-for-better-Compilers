
# Define some variables with different values, including None and empty string
name = "John Doe"
age = 30
is_student = False
my_variable = None
empty_string = ""

# Print out the type of each variable
print("Name: ", type(name))
print("Age: ", type(age))
print("Is student: ", type(is_student))
print("My Variable: ", type(my_variable))
print("Empty String: ", type(empty_string))

# Convert None to string
none_str = str(my_variable)
print("None as string: ", none_str)

# Convert other variables to strings using str() function or f-strings
age_str = str(age)
name_str = str(name)
is_student_str = str(is_student).lower() if is_student else "Not a student"
print("Age: ", age_str)
print("Name: ", name_str)
print("Is Student: ", is_student_str)
