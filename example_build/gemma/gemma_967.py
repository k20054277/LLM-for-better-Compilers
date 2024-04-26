
# Define a parent class called Employee
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        print("The salary of", self.name, "is", self.salary)

# Define a subclass called Manager that inherits from Employee
class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def calculate_salary(self):
        print("The salary of", self.name, "is", self.salary + self.bonus)

# Create an instance of the Employee class
employee = Employee("John Doe", 50000)

# Create an instance of the Manager class
manager = Manager("Jane Doe", 60000, 10000)

# Call the calculate_salary method for each instance
employee.calculate_salary()
manager.calculate_salary()

# Output:
# The salary of John Doe is 50000
# The salary of Jane Doe is 60000
