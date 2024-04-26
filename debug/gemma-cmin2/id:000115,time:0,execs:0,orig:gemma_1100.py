
# Demonstrating the use of as and with

# Define a class called Employee
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary * 1.1

# Create an instance of the Employee class
employee = Employee("John Doe", 50000)

# Use the as keyword to bind the employee object to the variable employee_salary
with employee:
    # Access the employee's salary
    salary = employee.calculate_salary()

# Print the salary
print("Salary:", salary)

# Output:
# Salary: 55000.0
