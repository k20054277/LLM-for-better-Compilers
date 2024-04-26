
class Student:
    def __init__(self, name=None, grade=None):
        self.name = name
        self.grade = grade

student1 = Student("John Doe")
student2 = Student(name="Jane Smith", grade=95)

print(student1.grade)  # Output: None
print(student2.grade)  # Output: 95
