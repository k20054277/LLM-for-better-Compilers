
# List of tuples representing student data
students_data = [("John Doe", 20, True), ("Jane Smith", 18, False), ("Mike Johnson", 22, True)]

# Function to check eligibility (age > 18 and is_student_active)
def check_eligibility(student):
    name, age, is_student_active = student
    return age > 18 and is_student_active

# Filter students based on given condition using filter and map along with enumerate
filtered_students = list(filter(check_eligibility, enumerate(students_data, 1)))

# print the name and index of eligible students
for index, student in enumerate(filtered_students):
    name, _ = student
    print(f"Student {index} is named {name}")
