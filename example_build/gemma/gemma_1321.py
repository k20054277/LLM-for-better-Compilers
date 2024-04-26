
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary

    def increase_salary(self, percentage):
        self.salary *= (1 + percentage)

# Create an instance of the Employee class
employee = Employee("John Doe", 50000)

# Assert that the employee's salary is 50000
assert employee.get_salary() == 50000

# Increase the employee's salary by 10%
employee.increase_salary(0.1)

# Assert that the employee's salary has increased to 55000
assert employee.get_salary() == 55000

# Print the employee's name and salary
print("Name:", employee.name)
print("Salary:", employee.get_salary())
