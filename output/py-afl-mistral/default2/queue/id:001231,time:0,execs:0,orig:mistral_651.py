
# Define a variable 'age' with an initial value of 18
age = 18

# A Boolean expression checking if age is greater than or equal to 18
is_adult = (age >= 18)

print("Is the person an adult?")
print(f"Answer: {is_adult}")

if is_adult:
    print("Access granted! You can vote and drive.")
else:
    print("Sorry, you're not old enough for those privileges yet.")

# Now we change the value of age to 21
age = 21
is_adult = (age >= 18)

print("\nIs the person an adult now?")
print(f"Answer: {is_adult}")
