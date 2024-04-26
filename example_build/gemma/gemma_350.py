
# False and next

x = False
y = 1

while not x:
    print(y)
    y += 1
    if y > 5:
        x = True

print("Finished!")
