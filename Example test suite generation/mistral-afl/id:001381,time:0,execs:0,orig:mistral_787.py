
# Initialize a boolean variable 'is_student_eligible' with value True
is_student_eligible = True

# Create an empty list 'student_list'
student_list = []

print("Is student eligible initially: ", is_student_eligible)

# Add some students to the list and check eligibility
if len(student_list) > 0:
    print("Students are present. Student eligibility: ", is_student_eligible)
    student_list.append("John")
    student_list.append("Mike")
    print("Students after adding two students: ", student_list)
    if len(student_list) > 2:
        print("With more than 2 students, student eligibility becomes False: ")
        is_student_eligible = False
else:
    print("No students present. Student eligibility remains as:", is_student_eligible)

# Remove some students and check eligibility
if len(student_list) > 0:
    student_list.pop()
    student_list.pop()
    print("Students after removing two students: ", student_list)
    if len(student_list) == 0:
        print("No more students present. Student eligibility remains as:", is_student_eligible)
    else:
        print("With fewer students, student eligibility might change based on the criteria.")
else:
    print("No students present. Student eligibility remains as:", is_student_eligible)
