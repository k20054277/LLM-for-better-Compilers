
# Define a class called Employee
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary

# Define a subclass called Manager of the Employee class
class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def get_salary(self):
        return self.salary + self.bonus

# Create an instance of the Manager class
manager = Manager("John Doe", 50000, 10000)

# Print the salary of the manager
print(manager.get_salary())

# Output: 60000
