
# Define a list of true and false values
true_false = [True, False, True, False, True]

# Use zip to iterate over the list and print True and False alternately
for true, false in zip(true_false, true_false):
    print(true, false)
