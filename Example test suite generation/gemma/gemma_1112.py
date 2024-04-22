
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_salary(cls, salary):
        return cls(name="John Doe", salary=salary)

    def get_salary(self):
        return self.salary

    def __str__(self):
        return f"Name: {self.name}, Salary: ${self.salary}"


# Create an employee object
employee = Employee.from_salary(50000)

# Print the employee's information
print(employee)

# Get the employee's salary
print(employee.get_salary())
