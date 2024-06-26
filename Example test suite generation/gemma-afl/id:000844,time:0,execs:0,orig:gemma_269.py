
import torch
import torch.nn as nn

# Define a simple linear regression model
model = nn.Linear(10, 1)

# Define the loss function
criterion = nn.MSELoss()

# Define the optimizer
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# Generate some sample data
x = torch.tensor([[1.0], [2.0], [3.0], [4.0], [5.0]])
y = torch.tensor([2.0, 4.0, 6.0, 8.0, 10.0])

# Train the model
for epoch in range(10):
    # Forward pass
    pred = model(x)
    loss = criterion(pred, y)

    # Backward pass
    optimizer.zero_grad()
    loss.backward()

    # Update weights
    optimizer.step()

# Print the final model parameters
print(model.state_dict())

# Make predictions
pred = model(x)
print(pred)
