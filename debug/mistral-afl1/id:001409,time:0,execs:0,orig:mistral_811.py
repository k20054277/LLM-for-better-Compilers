
# Sample data
numbers = [1, 2, 3, 4, 5]

# Lambda function to check if a number is even
is_even = lambda num: num % 2 == 0

# Filter the list using and with the lambda function
filtered_list = list(filter(lambda num: is_even(num) and num > 2, numbers))

print("Numbers greater than 2 and even:")
for num in filtered_list:
    print(num)
