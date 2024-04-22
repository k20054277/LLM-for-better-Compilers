
for i in range(1, 6):
    if i % 2 == 0:  # check if the current number is even (0 is left over when divided by 2)
        print(f"Found even number: {i}")
        break     # exit the loop once an even number is found
    else:
        print(f"Current number: {i}, which is odd")
