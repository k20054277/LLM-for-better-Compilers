
# Create a dictionary with some key-value pairs
my_dict = {
    "name": "John Doe",
    "age": 30,
    "is_student": False
}

# Use and operator to check if 'name' is 'John Doe' and 'age' is greater than 25
if my_dict["name"] == "John Doe" and my_dict["age"] > 25:
    print("Condition met!")
else:
    print("Condition not met.")

# Now let's check if the name is 'John Doe' and age is greater than or equal to 30 (or we can use 'is_student' as a condition)
if my_dict["name"] == "John Doe" and (my_dict["age"] >= 30 or not my_dict["is_student"]):
    print("Condition met!")
else:
    print("Condition not met.")
