
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary

    def set_salary(self, new_salary):
        if new_salary > 0:
            self.salary = new_salary
        else:
            print("Salary cannot be negative")


employee = Employee("John Doe", 50000)

print("Name:", employee.name)
print("Salary:", employee.get_salary())

employee.set_salary(60000)
print("Updated Salary:", employee.get_salary())

employee.set_salary(-10000)
print("Error:", employee.set_salary(-10000))
