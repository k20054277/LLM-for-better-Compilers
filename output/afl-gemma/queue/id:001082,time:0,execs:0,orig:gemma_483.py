
class Employee:
    def __init__(self, name, salary, email):
        self.name = name
        self.salary = salary
        self.email = email

    def get_salary(self):
        return self.salary

    def get_email(self):
        return self.email

    def set_salary(self, new_salary):
        self.salary = new_salary

    def set_email(self, new_email):
        self.email = new_email


# Create an employee object
employee = Employee("John Doe", 50000, "john.doe@example.com")

# Get the employee's salary and email
print("Name:", employee.name)
print("Salary:", employee.get_salary())
print("Email:", employee.get_email())

# Set the employee's salary and email
employee.set_salary(60000)
employee.set_email("john.doe.updated@example.com")

# Get the employee's updated salary and email
print("Updated Salary:", employee.get_salary())
print("Updated Email:", employee.get_email())

# None check
if employee.email is None:
    print("Email is not set")
