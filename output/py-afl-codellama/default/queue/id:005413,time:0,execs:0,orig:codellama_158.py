import torch

# create a tensor with some elements
tensor = torch.tensor([1, 2, 3, 4])

# use the and operator on two tensors
result = tensor & tensor

print(result)