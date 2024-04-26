
# Define a class called Employee
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary

# Create an instance of the Employee class called employee1
employee1 = Employee("John Doe", 50000)

# Check if employee1 is an instance of the Employee class
if isinstance(employee1, Employee):
    print("employee1 is an instance of the Employee class")

# Get the salary of employee1
salary = employee1.get_salary()

# Print the salary of employee1
print("The salary of employee1 is $", salary)

# Print the name of employee1
print("The name of employee1 is", employee1.name)
