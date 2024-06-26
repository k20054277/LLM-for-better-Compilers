
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary

    def increase_salary(self, percent):
        self.salary *= (1 + percent)

# Create an instance of the Employee class
employee = Employee("John Doe", 50000)

# Get the employee's salary
print(employee.get_salary())

# Increase the employee's salary by 10%
employee.increase_salary(0.1)

# Get the employee's new salary
print(employee.get_salary())
