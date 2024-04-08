
# This program goes through numbers from 0 to 9, and prints only even numbers

for i in range(10):
    if i % 2 != 0:  # Check if current number is odd
        continue   # If it's odd, jump to the next iteration of the loop
    print(i)      # If it's even, print it
