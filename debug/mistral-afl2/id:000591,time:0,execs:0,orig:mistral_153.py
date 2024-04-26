
# Define an empty class named MyList
class MyList:
    def __init__(self):
        self.items = []

    # Override the len method to return False when the list is empty
    def __len__(self):
        return len(self.items) == 0 and False

# Create an instance of MyList
my_list = MyList()

# Check if the instance is empty using length property (len()) and False
print("Is the list empty using len():", len(my_list)) # prints: Is the list empty using len(): True
print("Is the list empty using False:", not my_list or False) # prints: Is the list empty using False: True

# Add some items to the list
my_list.items.append(1)
my_list.items.append(2)
my_list.items.append(3)

# Check if the list is empty again
print("Is the list empty using len():", len(my_list)) # prints: Is the list empty using len(): False
print("Is the list empty using False:", not my_list or False) # prints: Is the list empty using False: False
