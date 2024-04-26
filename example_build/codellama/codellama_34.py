# Print "Hello, World!" if the input number is even and 10 or less
input_number = int(input("Enter a number: "))
if input_number % 2 == 0 and input_number <= 10:
    print("Hello, World!")
else:
    print("Goodbye")