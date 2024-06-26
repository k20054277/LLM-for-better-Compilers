
import random

def roll_dice(num_rolls=1):
    """Roll a dice for given number of times."""
    result = []
    for _ in range(num_rolls):
        rolled_number = random.randint(1, 6)
        result.append(rolled_number)
    return result

def sum_of_dice_rolls(rolls):
    """Calculate the sum of all the dice rolls."""
    return sum(rolls)

if __name__ == "__main__":
    # Rolling dice 5 times and checking the sum is between 7 and 13.
    rolls = roll_dice()
    assert 7 <= sum_of_dice_rolls(rolls) <= 13, "Sum of dice rolls should be between 7 and 13"

    print("Rolled: ", rolls)
    print("Sum: ", sum_of_dice_rolls(rolls))
