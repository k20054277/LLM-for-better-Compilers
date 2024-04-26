
# Define a boolean variable 'is_student' and initialize it to True
is_student = True

# Define a tuple 'student_info' with some student data
student_info = ("John Doe", 19, "Computer Science")

# Function to check if the given person is a student or not
def is_student_check(person, student_info):
    return person == student_info[0] and isinstance(is_student, bool)

# Testing the function with some inputs
print("Is John Doe a student? ", is_student_check("John Doe", student_info)) # Output: Is John Doe a student?  True
print("Is Michael Jackson a student? ", is_student_check("Michael Jackson", student_info)) # Output: Is Michael Jackson a student?  False
