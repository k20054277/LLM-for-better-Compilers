
# Initialize variable 'num' with value 0
num = 0

# Loop while num is less than 10
while num < 10:
    # Multiply num by 2 using *= and check if the result is still less than 10
    num *= 2
    
    # Check if the new value of num is still less than 10 using Boolean value True
    if num >= 10:
        print("Number exceeded limit, loop will terminate.")
        break
    
# Print the final value of 'num'
print(f"The number is now {num}.")
