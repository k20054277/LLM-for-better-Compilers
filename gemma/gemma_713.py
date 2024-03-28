
import torch
import torch.nn as nn

# Define a simple linear regression model
model = nn.Linear(10, 1)

# Define a loss function
criterion = nn.MSELoss()

# Define an optimizer
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# Generate some sample data
x = torch.tensor([1, 2, 3, 4, 5])
y = torch.tensor([10, 12, 14, 16, 18])

# Train the model
for epoch in range(10):
    # Forward pass
    y_pred = model(x)
    loss = criterion(y_pred, y)

    # Backward pass
    optimizer.zero_grad()
    loss.backward()

    # Update weights
    optimizer.step()

# Print the model's parameters
print(model.parameters())

# Make a prediction
y_pred = model(x)
print(y_pred)
