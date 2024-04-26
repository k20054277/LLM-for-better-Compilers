
def demo_and_delattr():
    class Employee:
        def __init__(self, name, salary):
            self.name = name
            self.salary = salary

        def __and__(self, other):
            print("And operation!")
            return self

        def __delattr__(self, attr):
            print("Delattr operation!")
            print("Attribute:", attr)
            delattr(self, attr)

    emp = Employee("John Doe", 50000)

    # And operation
    emp and Employee("Jane Doe", 60000)

    # Delattr operation
    delattr(emp, "salary")

    # Print attributes after delattr operation
    print("Name:", emp.name)
    print("Salary:", emp.salary)

if __name__ == "__main__":
    demo_and_delattr()
