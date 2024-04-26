
# This Python program demonstrates the use of True and isinstance

# Define a class called Employee
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary

# Create an instance of the Employee class
employee = Employee("John Doe", 50000)

# Check if the employee object is an instance of the Employee class
if isinstance(employee, Employee):
    print("Employee object is an instance of the Employee class")

# Check if the employee object is True
if employee:
    print("Employee object is True")

# Print the employee's salary
print("Employee salary:", employee.get_salary())
