
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary

    def set_salary(self, new_salary):
        self.salary = new_salary

    def __str__(self):
        return f"Name: {self.name}, Salary: ${self.salary}"


# Create an employee object
employee = Employee("John Doe", 50000)

# Print the employee's information
print(employee)

# Get the employee's salary
salary = employee.get_salary()

# Print the salary
print(salary)

# Set the employee's salary to 60000
employee.set_salary(60000)

# Print the employee's information after the salary change
print(employee)
