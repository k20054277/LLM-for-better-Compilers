
True and with statement

# Define a class called Employee
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary * 1.1

# Create an instance of the Employee class
employee = Employee("John Doe", 50000)

# Use True and with statement to calculate employee's salary
with True:
    salary = employee.calculate_salary()
    print("Employee's salary:", salary)

# Output
# Employee's salary: 55000
