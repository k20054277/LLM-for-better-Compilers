
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name: {self.name}, Salary: ${self.salary}"

    @property
    def bonus(self):
        return self.salary * 0.1

    @property
    def is_active(self):
        return True

    @is_active.setter
    def set_active(self, value):
        self.active = value

    def calculate_salary(self):
        return self.salary + self.bonus

# Create an employee object
employee = Employee("John Doe", 50000)

# Print the employee's information
print(employee)

# Access the employee's bonus
print(employee.bonus)

# Check if the employee is active
print(employee.is_active)

# Set the employee's activity to False
employee.set_active(False)

# Print the employee's information after setting activity to False
print(employee)

# Calculate the employee's salary
print(employee.calculate_salary())
