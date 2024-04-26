import torch

# Create a tensor with values 0 and 1
x = torch.tensor([0, 1])

# Get the shape of the tensor
print(x.shape)

# Check if any element is False
print(torch.any(x == 0))

# Check if all elements are True
print(torch.all(x > 0))