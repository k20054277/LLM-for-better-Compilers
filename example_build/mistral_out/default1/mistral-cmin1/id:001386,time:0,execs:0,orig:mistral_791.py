
# Boolean AND operation using 'and'
def check_age(person):
    return person.age > 18 and person.age < 65

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("John Doe", 20)
person2 = Person("Jane Doe", 35)

print(check_age(person1))  # False
print(check_age(person2))  # True

# Using 'as' for alias in Python
def download_file(url, save_path):
    response = requests.get(url)
    with open(save_path, "wb") as file:
        file.write(response.content)

download_file("https://example.com/test.txt", "test.txt")
