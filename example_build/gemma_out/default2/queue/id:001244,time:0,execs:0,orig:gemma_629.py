
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary

    @classmethod
    def from_salary(cls, salary):
        return cls(name="John Doe", salary=salary)

# Create an instance of the Employee class
employee = Employee("John Doe", 50000)

# Access the employee's salary
print(employee.get_salary())  # Output: 50000

# Create an instance of the Employee class from the classmethod
employee2 = Employee.from_salary(salary=60000)

# Access the employee's salary
print(employee2.get_salary())  # Output: 60000

# Print the employee's name
print(employee.name)  # Output: John Doe
