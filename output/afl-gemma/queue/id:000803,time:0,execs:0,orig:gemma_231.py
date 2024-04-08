
# Define a class called Employee
class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def __str__(self):
        return f"Name: {self.name}, Salary: ${self.salary}, Department: {self.department}"

    def set_salary(self, new_salary):
        self.salary = new_salary

# Create an instance of the Employee class
employee = Employee("John Doe", 50000, "Sales")

# Print the employee's information
print(employee)

# Set the employee's salary to 60000
employee.set_salary(60000)

# Print the employee's information after the salary has been updated
print(employee)
