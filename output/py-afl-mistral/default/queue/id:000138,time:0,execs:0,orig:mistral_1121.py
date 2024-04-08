
class Person:
    def __init__(self, first_name, last_name):
        self.first = first_name
        self.last = last_name

# create a new instance of the Person class
person = Person("John", "Doe")

# use 'as' to assign an alias to an existing attribute
alias_for_first = asname = person.first

# print out the aliases to demonstrate they are equivalent to original attributes
print(f"Alias for first name: {alias_for_first}")
print(f"Original first name: {person.first}")

# use 'setattr' to change the value of an attribute
setattr(person, "last", "Smith")

# print out the changed last name and the new alias (if applicable)
print(f"Last name: {person.last}")
print(f"Alias for last name (nonexistent in this case): {asname}")
