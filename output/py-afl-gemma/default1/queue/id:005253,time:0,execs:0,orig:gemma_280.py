
# False and break demonstration

for i in range(10):
    if i is 5:
        print("Reached number 5!")
        break
    elif i is False:
        print("Reached False!")
        break
    else:
        print(i)
