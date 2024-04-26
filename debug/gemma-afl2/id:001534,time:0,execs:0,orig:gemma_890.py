
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary

    def __str__(self):
        return f"Name: {self.name}, Salary: ${self.salary}"


class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def get_salary(self):
        return self.salary + self.bonus

    def __str__(self):
        return f"Name: {self.name}, Salary: ${self.salary}, Bonus: ${self.bonus}"


# Create an employee object
employee = Employee("John Doe", 50000)

# Create a manager object
manager = Manager("Jane Doe", 60000, 10000)

# Print the employee and manager objects
print(employee)
print(manager)
