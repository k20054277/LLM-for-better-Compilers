
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @staticmethod
    def get_minimum_salary():
        return 10000

    def calculate_salary(self):
        return self.salary + self.get_minimum_salary()

# Create an instance of the Employee class
employee = Employee("John Doe", 5000)

# Get the minimum salary
print(Employee.get_minimum_salary())

# Calculate the salary of the employee
print(employee.calculate_salary())

# Print the name and salary of the employee
print("Name:", employee.name)
print("Salary:", employee.salary)
