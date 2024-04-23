import torch

# Create a tensor with some values
tensor = torch.randn(5)

# Set some elements of the tensor to None
tensor[2] = None

print(tensor)
# Output: tensor([0, 1, None, 3, 4])