
# True and requirements.txt

# Define a boolean variable
is_active = True

# If True, print "Active"
if is_active:
    print("Active")

# Create a requirements.txt file
with open("requirements.txt", "w") as f:
    f.write("Flask")
    f.write("\n")
    f.write("Flask-SQLAlchemy")

# Print the contents of requirements.txt
with open("requirements.txt") as f:
    print(f.read())
