
# True and garbage collection demonstration

# Define a class to illustrate garbage collection
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __del__(self):
        print("Goodbye, ", self.name)

# Create an employee object
employee = Employee("John Doe", 50000)

# Assign the employee object to a variable
employee_var = employee

# Do some operations on the employee object
employee_var.salary = 60000

# The variable goes out of scope, and the employee object is garbage collected
del employee_var

# The destructor method of the employee object is called, printing "Goodbye, John Doe"
