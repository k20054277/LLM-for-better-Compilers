
# Define a class called Employee
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary

    def increase_salary(self, percentage):
        self.salary = self.salary * (1 + percentage)


# Create a list of employees
employees = [
    Employee("John Doe", 50000),
    Employee("Jane Doe", 60000),
    Employee("Peter Pan", 70000)
]

# Print the salaries of each employee
for employee in employees:
    print(employee.get_salary())

# Increase the salary of each employee by 10%
for employee in employees:
    employee.increase_salary(0.1)

# Print the salaries of each employee after the increase
for employee in employees:
    print(employee.get_salary())
