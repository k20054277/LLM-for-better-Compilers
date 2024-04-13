
# Demonstrate the use of None and **=

# Define a function
def demo(x):
    # Use None as a default parameter
    if x is None:
        x = 10

    # Use **= to assign a default value
    else:
        x *= 2

    # Print the value of x
    print(x)


# Call the function with different arguments
demo(None)  # Output: 10
demo(5)  # Output: 10
demo(10)  # Output: 20

# Example using None and **= in a class

class Employee:
    def __init__(self, name, salary=None):
        self.name = name
        self.salary = salary

    def get_salary(self):
        # Use None checking before assigning a default value
        if self.salary is None:
            self.salary = 20000

        # Return the salary
        return self.salary

# Create an employee object
employee = Employee("John Doe")

# Print the employee's salary
print(employee.get_salary())  # Output: 20000

# Modify the employee's salary
employee.salary = 30000

# Print the employee's salary after modification
print(employee.get_salary())  # Output: 30000
