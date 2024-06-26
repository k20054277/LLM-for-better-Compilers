
import subprocess
import os

def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

numbers = [1, 2, 3, 4]
result = calculate_sum(numbers)
assert result == 10, "The sum of the given numbers is not equal to 10"
print("The sum of the given numbers is:", result)

command = 'echo "Hello World"'
process = subprocess.run(command, shell=True, capture_output=True)
assert process.returncode == 0, f"Command '{command}' returned non-zero status {process.returncode}"
print("Output from command:", process.stdout.decode())
