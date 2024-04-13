import torch

# Define a tensor with values 0, 1, and 2
t = torch.tensor([0, 1, 2])

# Use the `True` method to find all elements in the tensor that are greater than 1
greater_than_one = t.gt(1)
print(greater_than_one) # Output: tensor([False, True, True])

# Use the `True` method with a parameter to find all elements in the tensor that are greater than or equal to 1
greater_than_or_equal_to_one = t.ge(1)
print(greater_than_or_equal_to_one) # Output: tensor([True, True, True])

# Use the `False` method to find all elements in the tensor that are less than 1
less_than_one = t.lt(1)
print(less_than_one) # Output: tensor([False, False, True])

# Use the `False` method with a parameter to find all elements in the tensor that are less than or equal to 1
less_than_or_equal_to_one = t.le(1)
print(less_than_or_equal_to_one) # Output: tensor([True, False, True])