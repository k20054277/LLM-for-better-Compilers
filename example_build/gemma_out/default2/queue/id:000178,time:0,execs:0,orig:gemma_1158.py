
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name: {self.name}, Salary: ${self.salary}"

    def increase_salary(self, percentage):
        self.salary *= (1 + percentage)
        print(f"Salary increased by {percentage}% to ${self.salary}")


employee = Employee("John Doe", 50000)
employee.increase_salary(10)

print(employee)
