
# False and OOP

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary * 1.1

    def __str__(self):
        return f"Name: {self.name}, Salary: ${self.salary}"


# Create an Employee object
employee = Employee("John Doe", 50000)

# Check if the employee is eligible for a raise
eligible = False

# If the employee is not eligible for a raise, print an error message
if not eligible:
    print("Error: Employee is not eligible for a raise.")

# Otherwise, print the employee's salary after the raise
else:
    print(f"Salary after raise: ${employee.calculate_salary()}")

# Print the employee's information
print(f"Employee information: \n{employee}")
