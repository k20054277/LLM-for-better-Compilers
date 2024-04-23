
def my_class():
    pass

my_class.__dict__['name'] = 'John Doe'
my_class.__dict__['age'] = 30

print(my_class.name)  # Output: John Doe
print(my_class.age)  # Output: 30

delattr(my_class, 'name')

print(my_class.name)  # Output: None
print(my_class.age)  # Output: 30
