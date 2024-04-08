
import pytorch
import numpy as np

# Define a PyTorch tensor
x = pytorch.tensor(np.arange(10))

# Check if the tensor is False
print(x.is_false())

# Set the tensor to False
x.fill_(False)

# Check if the tensor is False
print(x.is_false())

# Print the tensor
print(x)
