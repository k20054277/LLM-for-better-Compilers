
import torch
import torch.nn as nn

# Define a simple linear layer
model = nn.Linear(10, 20)

# Create a tensor
x = torch.randn(10)

# Apply the linear layer to the tensor
y = model(x)

# Print the output
print(y)
