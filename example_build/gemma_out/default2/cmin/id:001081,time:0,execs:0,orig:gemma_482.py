
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary

    def __str__(self):
        return f"Name: {self.name}, Salary: ${self.salary}"


class Manager(Employee):
    def calculate_salary(self):
        return self.salary + 10000

    def __str__(self):
        return f"Name: {self.name}, Salary: ${self.salary}"


# Create an employee object
employee = Employee("John Doe", 50000)

# Create a manager object
manager = Manager("Jane Doe", 60000)

# Print the employee and manager objects
print(employee)
print(manager)

# Check if the employee object is None
if employee is None:
    print("Employee object is None")

# Check if the manager object is None
if manager is None:
    print("Manager object is None")

# Check if the employee salary is None
if employee.salary is None:
    print("Employee salary is None")

# Check if the manager salary is None
if manager.salary is None:
    print("Manager salary is None")
