
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name: {self.name}, Salary: ${self.salary}"

    @classmethod
    def from_salary(cls, salary):
        return cls(name="John Doe", salary=salary)

# Create an instance of the Employee class
employee = Employee.from_salary(50000)

# Print the employee information
print(employee)

# Output:
# Name: John Doe, Salary: $50000