
# Demonstrating True and delattr

class Employee:
    name = "John Doe"
    salary = 50000

    def __init__(self, company):
        self.company = company

    def __del__(self):
        print("Employee", self.name, "has left the company.")

    def get_salary(self):
        return self.salary

    def set_salary(self, new_salary):
        self.salary = new_salary


# Create an instance of the Employee class
employee = Employee("Tech Corp")

# Access and modify employee attributes
print("Name:", employee.name)
print("Salary:", employee.get_salary())
employee.set_salary(60000)
print("Updated Salary:", employee.get_salary())

# Delete the employee object
del employee

# Output
# Name: John Doe
# Salary: 50000
# Updated Salary: 60000
# Employee John Doe has left the company.
