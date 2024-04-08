
# Define some variables
num = 0
is_rainy = False
is_sunny = True

print("Initial values:")
print("Num: ", num)
print("Is it raining?: ", is_rainy)
print("Is it sunny?: ", is_sunny)

# Test some conditions
if not is_rainy:
    print("\nIf it's not raining, then...")
    if num > 0:
        print("Num is positive.")
    else:
        print("Num is zero or negative.")
else:
    print("\nIf it's raining, then...")
    
# Test more conditions
if not (is_rainy and is_sunny):
    print("\nIf it's either raining OR sunny but not both, then...")

# Test an 'and' condition
if is_rainy and num > 0:
    print("\nIf it's raining AND Num is positive, then this condition will NOT be met.")
else:
    print("Otherwise, the condition is true.")
