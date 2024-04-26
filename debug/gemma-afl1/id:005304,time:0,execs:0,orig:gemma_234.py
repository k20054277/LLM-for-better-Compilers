
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @staticmethod
    def calculate_bonus(salary):
        return salary * 0.1

    def calculate_total_salary(self):
        return self.salary + Employee.calculate_bonus(self.salary)

# Create an instance of the Employee class
employee = Employee("John Doe", 50000)

# Calculate the total salary
total_salary = employee.calculate_total_salary()

# Print the total salary
print("Total salary:", total_salary)
