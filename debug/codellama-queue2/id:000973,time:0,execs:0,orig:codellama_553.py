# requirements.txt
numpy==1.20.3
scipy==1.7.3

# main.py
import numpy as np
from scipy import stats

def calculate_mean(numbers):
    if not numbers:  # Check if the list is empty
        return None
    return np.mean(numbers)

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    mean = calculate_mean(numbers)
    print(f"The mean of the list is {mean}")