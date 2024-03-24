
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @staticmethod
    def calculate_salary(salary):
        return salary * 1.1

    def get_salary(self):
        return self.salary

    def get_name(self):
        return self.name


# Create an instance of the Employee class
employee = Employee("John Doe", 50000)

# Access the static method
salary_with_increase = Employee.calculate_salary(employee.salary)

# Print the salary with increase
print("Salary with increase:", salary_with_increase)

# Print the employee's name and salary
print("Name:", employee.get_name())
print("Salary:", employee.get_salary())
