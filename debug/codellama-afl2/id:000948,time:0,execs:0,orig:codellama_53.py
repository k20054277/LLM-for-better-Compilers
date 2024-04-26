def check_age(age):
    return age >= 18 and age <= 25

# Test the function
if check_age(19):
    print("You are eligible to vote.")
else:
    print("Sorry, you are not eligible to vote yet.")