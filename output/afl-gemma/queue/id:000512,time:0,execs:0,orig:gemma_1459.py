
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary

    def set_salary(self, new_salary):
        self.salary = new_salary

# Create an employee object
employee = Employee("John Doe", 50000)

# Assert that the employee's salary is 50000
assert employee.get_salary() == 50000

# Set the employee's salary to 60000
employee.set_salary(60000)

# Assert that the employee's salary has changed to 60000
assert employee.get_salary() == 60000

# Print the employee's name and salary
print("Employee name:", employee.name)
print("Employee salary:", employee.get_salary())
