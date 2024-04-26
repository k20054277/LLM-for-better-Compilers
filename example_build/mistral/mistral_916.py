
import numpy as np
import torch

# Create NumPy arrays
np_arr1 = np.array([[1, 0, 1], [1, 1, 1]], dtype=bool)
np_arr2 = np.ones((2, 3), dtype=bool)

print("NumPy Array 1:")
print(np_arr1)
print("\nNumPy Array 2:")
print(np_arr2)

# Perform NumPy logical AND operation
np_and = np.logical_and(np_arr1, np_arr2)
print("\nNumPy Logical AND:\n")
print(np_and)

# Create PyTorch tensors from NumPy arrays
torch_arr1 = torch.from_numpy(np_arr1).float()
torch_arr2 = torch.from_numpy(np_arr2).float()

print("\nPyTorch Tensors:")
print("Tensor 1:")
print(torch_arr1)
print("Tensor 2:")
print(torch_arr2)

# Perform PyTorch element-wise AND operation
torch_and = torch.logical_and(torch_arr1, torch_arr2)
print("\nPyTorch Logical AND:\n")
print(torch_and)
