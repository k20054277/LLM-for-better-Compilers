
import torch
import torch.nn as nn
import torch.optim as optim

# Define a simple 2-input XOR gate function
def xor(x):
    return torch.tensor([[1 if (i[0] and not i[1]) or (not i[0] and i[1]) else 0 for i in x]], dtype=torch.float32)

# Define a simple neural network for XOR gate using PyTorch
class SimpleNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(2, 4)
        self.fc2 = nn.Linear(4, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.sigmoid(self.fc2(x))
        return x

# Create a dataset for training the neural network
X = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=torch.float32)
Y = torch.tensor([[0], [1], [1], [0]], dtype=torch.float32)

# Create the neural network model and define the loss function and optimizer
model = SimpleNN()
criterion = nn.BCELoss()  # Binary Cross Entropy Loss
optimizer = optim.SGD(model.parameters(), lr=0.5)

# Train the model for 10 epochs
for epoch in range(1, 11):
    # Forward pass
    outputs = model(X)
    loss = criterion(outputs, Y)

    # Backward pass and optimization
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    print('Epoch [{}/{}], Loss: {:.4f}'.format(epoch, 10, loss.item()))
