
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

# Get the employee's salary
print(employee.get_salary())  # Output: 50000

# Set the employee's salary
employee.set_salary(60000)

# Get the employee's salary after setting it
print(employee.get_salary())  # Output: 60000
