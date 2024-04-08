
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary

    def raise_salary(self, percentage):
        self.salary *= (1 + percentage)

# Create an instance of the Employee class
employee = Employee("John Doe", 50000)

# Print the employee's salary
print(employee.get_salary())

# Raise the employee's salary by 10%
employee.raise_salary(0.1)

# Print the employee's salary after the raise
print(employee.get_salary())

# Output:
# 50000
# 55000
