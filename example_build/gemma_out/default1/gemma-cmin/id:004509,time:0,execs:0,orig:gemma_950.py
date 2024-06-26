
import torch
import torch.nn as nn

# Define a simple linear regression model
model = nn.Linear(10, 1)

# Define a simple loss function
criterion = nn.MSELoss()

# Define a simple optimizer
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# Generate some sample data
x = torch.randn(10, 1)
y = torch.randn(10, 1)

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

# Print the final model parameters
print(model.parameters())

# Plot the learned function
import matplotlib.pyplot as plt
plt.scatter(x, y)
plt.plot(x, y_pred.detach())
plt.show()
