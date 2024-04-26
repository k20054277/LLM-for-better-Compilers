
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property
    def salary(self):
        print("Getting salary...")
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        print("Setting salary...")
        self._salary = new_salary

# Create an instance of the Employee class
employee = Employee("John Doe", 50000)

# Get the employee's salary
print(employee.salary)

# Set the employee's salary
employee.salary = 60000

# Get the employee's salary again
print(employee.salary)
