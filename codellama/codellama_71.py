def get_age(name):
    try:
        age = int(input("What is {}'s age? ".format(name)))
        if age < 0:
            raise ValueError("Age must be non-negative")
        return age
    except ValueError as e:
        print("Invalid input. Error: {}".format(e))