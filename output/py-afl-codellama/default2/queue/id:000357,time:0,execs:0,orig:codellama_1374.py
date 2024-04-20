import torch

# Define a PyTorch tensor
x = torch.tensor([1, 2, 3])

# Use assert to check that the tensor has the expected shape
assert x.shape == (3,)

# Use assert to check that the tensor has the expected values
assert x[0] == 1 and x[1] == 2 and x[2] ==