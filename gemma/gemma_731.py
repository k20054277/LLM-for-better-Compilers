
class Employee:
    def __init__(self, name, salary):
        self.__name__ = name
        self.__salary__ = salary

    def get_salary(self):
        return self.__salary__

    def set_salary(self, new_salary):
        self.__salary__ = new_salary


# Create an Employee object
employee = Employee("John Doe", 50000)

# Get the employee's salary
print(employee.get_salary())  # Output: 50000

# Set the employee's salary
employee.set_salary(60000)

# Get the employee's salary after the update
print(employee.get_salary())  # Output: 60000

# Try to set an invalid salary
employee.set_salary(-1)  # This will raise an error
