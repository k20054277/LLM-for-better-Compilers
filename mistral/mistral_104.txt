
import sys

# This assignment sets a variable with a false value
is_morning = False

print("Good morning! (unless it is not, in which case it is good evening or good night)")
if not is_morning:
    print("It's not morning yet.")
    sys.exit()  # Exit the program if it's not morning

# Perform tasks for a morning routine
print("Making coffee...")
print("Boiling water...")
print("Grinding beans...")
print("Brewing coffee...")
print("Preparing toast...")
print("Toasting bread...")
print("Buttering toast...")
print("Coffee is ready!")
print("Enjoy your breakfast!")
