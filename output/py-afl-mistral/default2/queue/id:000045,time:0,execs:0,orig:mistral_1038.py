
# List of tuples containing numbers and their squares
data = [(i, i * i) for i in range(1, 6)]

# Outer loop through the list of tuples
for num, sqr in data:
    print("Number:", num)
     for power in range(3, 10):
         # Calculate and assign result to a variable using 'as' keyword
         result = num ** power
         
         if result > 125:  # Condition to break the inner loop
             print("\nNumber {} exceeds 125 raised to any power in this loop".format(num))
             break

         print("Power: {0} Result: {1}".format(power, result))
     print()
