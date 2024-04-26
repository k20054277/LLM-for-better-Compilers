import torch

# Create a tensor with values 0 and 1
x = torch.tensor([[0, 1], [1, 0]])

# Use False to create a tensor with all zeros
y = torch.zeros(2, 2)

# Use the `where` method to set the elements of y equal to x where they are nonzero
y.where_(x)

print(y)