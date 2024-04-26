
# This Python program demonstrates the use of and and hasattr functions

# Define a class called Employee
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary

# Create an instance of the Employee class
employee = Employee("John Doe", 50000)

# Check if the employee has a salary attribute and if its value is greater than 40000
if hasattr(employee, "salary") and employee.salary > 40000:
    print("The employee's salary is greater than 40000.")

# Check if the employee has a salary attribute
if hasattr(employee, "salary"):
    print("The employee has a salary attribute.")

# Print the employee's name and salary
print("Name:", employee.name)
print("Salary:", employee.get_salary())
