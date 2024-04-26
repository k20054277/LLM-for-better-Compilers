
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary

    @classmethod
    def from_salary(cls, salary):
        return cls(name="John Doe", salary=salary)

    @staticmethod
    def calculate_bonus(salary):
        return salary * 0.1

# Create an instance of the Employee class
employee = Employee("Jane Doe", 50000)

# Access the employee's salary
print(employee.get_salary())

# Create an employee from a salary
employee2 = Employee.from_salary(salary=60000)

# Print the employee's name
print(employee2.name)

# Calculate the employee's bonus
bonus = Employee.calculate_bonus(salary=employee.salary)

# Print the bonus
print(bonus)
