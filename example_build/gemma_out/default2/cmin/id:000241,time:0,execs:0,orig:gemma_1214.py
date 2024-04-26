
class Employee:

    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def get_salary(self):
        return self.salary

    def get_department(self):
        return self.department

    def __str__(self):
        return f"Name: {self.name}, Salary: ${self.salary}, Department: {self.department}"


# Create an instance of the Employee class
employee = Employee("John Doe", 50000, "Sales")

# Access the attributes of the employee using the encapsulation methods
print(f"Name: {employee.get_name()}")
print(f"Salary: ${employee.get_salary()}")
print(f"Department: {employee.get_department()}")

# Print the employee object
print(str(employee))
