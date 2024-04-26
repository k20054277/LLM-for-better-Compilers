
# None and OOP demonstration

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary

    def increase_salary(self, percentage):
        self.salary = self.salary * (1 + percentage)

# Creating an employee object
employee = Employee("John Doe", 50000)

# Accessing employee salary
print("Employee salary:", employee.get_salary())

# Increasing employee salary by 10%
employee.increase_salary(0.1)

# Accessing updated employee salary
print("Updated employee salary:", employee.get_salary())

# Checking for None
if employee.salary is None:
    print("Salary is not None")

# Setting salary to None
employee.salary = None

# Checking for None again
if employee.salary is None:
    print("Salary is None")

# Output
# Employee salary: 50000
# Updated employee salary: 55000
# Salary is not None
# Salary is None
