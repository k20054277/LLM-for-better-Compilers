import torch

# Define two variables to be used in the logical operation
a = 5
b = 10

# Use the "and" operator to perform a logical AND operation on the two variables
c = a and b
print(c) # Output: True

# Use PyTorch to create a tensor with values [True, False]
d = torch.tensor([True, False])

# Use the "and" operator to perform a logical AND operation on the tensor
e = d and d[0]
print(e) # Output: True