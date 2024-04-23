# Create a list of possible answers
answers = ["yes", "no"]

# Prompt the user for their answer
answer = input("Do you like cats? ")

# Use the and operator to check if the user's answer is in the list of possible answers
if answer.lower() == "yes" and answer in answers:
    print("Great, I'm glad you like cats!")
else:
    print("Sorry, it looks like you didn't answer the question correctly.")