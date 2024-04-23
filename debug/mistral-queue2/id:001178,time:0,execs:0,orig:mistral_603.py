
import random

def flip_coin():
    """
    Simulates flipping a coin by returning either True or False with equal probability.
    """
    return random.choice([True, False])

if __name__ == "__main__":
    num_trials = 10
    print(f"Flipping a coin {num_trials} times:")
    for _ in range(num_trials):
        result = flip_coin()
        print(result)
