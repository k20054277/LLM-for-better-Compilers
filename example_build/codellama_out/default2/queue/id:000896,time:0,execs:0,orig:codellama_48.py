# Testing the use of "and" and "as" in Python

age = 21

if age >= 18 and age <= 25:
    print("You are eligible for a driver's license.")

license_type = "A" if age > 30 else "B"
print(f"Your license type is {license_type}.")