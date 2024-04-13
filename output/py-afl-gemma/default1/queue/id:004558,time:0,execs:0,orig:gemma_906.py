
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        if new_salary > 50000:
            print("Error: Salary cannot exceed $50,000")
        else:
            self._salary = new_salary


# Create an instance of the Employee class
employee = Employee("John Doe", 40000)

# Get the employee's salary
print("Employee's salary:", employee.salary)

# Set the employee's salary to $50,000
employee.salary = 50000

# Get the employee's salary after setting it to $50,000
print("Employee's salary:", employee.salary)

# Try to set the employee's salary to $60,000
employee.salary = 60000

# Output
# Employee's salary: 40000
# Employee's salary: 50000
# Error: Salary cannot exceed $50,000
