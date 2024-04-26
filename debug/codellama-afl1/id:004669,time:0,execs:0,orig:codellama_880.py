message = "Hello, World!"
for i in range(len(message)):
    if message[i].isalpha() and ord(message[i]) >= 65 and ord(message[i]) <= 90:
        print(f"The {i}th character of the string is a capital letter.")