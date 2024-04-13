
# This Python program demonstrates the use of and and isinstance operators.

# Define a class called Employee.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

# Create an instance of the Employee class.
employee = Employee("John Doe", 50000)

# Check if employee is an instance of the Employee class.
if employee instanceof Employee:
    print("Employee is an instance of the Employee class.")

# Check if employee's salary is greater than 40000.
if employee.salary > 40000 and employee.salary < 60000:
    print("Employee's salary is greater than 40000 and less than 60000.")

# Print employee's name and salary.
print("Employee's name:", employee.name)
print("Employee's salary:", employee.salary)
