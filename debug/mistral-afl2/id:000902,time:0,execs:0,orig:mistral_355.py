
import random

# Let's define a function that returns a random number or None
def get_random_number():
    return random.randint(0, 10) if random.random() > 0.5 else None

# Now let's create a list of random numbers and None values
numbers = [get_random_number() for i in range(10)]

print("List of random numbers and None:")
for num in numbers:
    print(num) if num is not None else print("None")

# Let's also create a list of 5 random numbers between 1 and 10
random_numbers = [random.randint(1, 10) for i in range(5)]
print("\nList of 5 random numbers between 1 and 10:")
for num in random_numbers:
    print(num)
