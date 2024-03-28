# Demonstrate the use of False and : in Python

age = input("Enter your age: ")

if age < 18:
    print("You are underage.")
elif age == 18 or age == 19:
    print("You are 18 or 19 years old.")
else:
    print("You are an adult.")