
# Define a class called Employee
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary


# Create an instance of the Employee class
employee = Employee("John Doe", 50000)

# Assert that the employee's salary is 50000
assert employee.get_salary() == 50000

# Assert that the employee is an instance of the Employee class
assert isinstance(employee, Employee)

# Print the employee's name and salary
print("Name:", employee.name)
print("Salary:", employee.salary)
