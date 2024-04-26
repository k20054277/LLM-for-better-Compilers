
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary

    def print_name(self):
        print(self.name)


class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def get_salary(self):
        return self.salary + self.bonus

    def print_name(self):
        print(self.name)


employees = [Employee("John Doe", 50000), Manager("Jane Doe", 60000, 10000)]

for employee in employees:
    employee.print_name()
    print(employee.get_salary())
    print()
