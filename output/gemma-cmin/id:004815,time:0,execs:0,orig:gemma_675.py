
def demonstrate_true_and_setattr():
    # Create a class
    class Employee:
        def __init__(self, name, salary):
            self.name = name
            self.salary = salary

    # Create an instance of the class
    employee = Employee("John Doe", 50000)

    # Use True to check if the salary is greater than 40000
    if employee.salary > 40000:
        # Use setattr to change the salary
        setattr(employee, "salary", 60000)

    # Print the updated salary
    print("Name:", employee.name)
    print("Salary:", employee.salary)

demonstrate_true_and_setattr()
