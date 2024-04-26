
import torch
import torch.nn as nn
import torch.optim as optim

# Define a simple neural network architecture
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(1, 4)
        self.fc2 = nn.Linear(4, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.sigmoid(self.fc2(x))
        return x

# Generate some random data for training and testing the network
data = torch.randn(1000, 1)
labels = torch.bernoulli(torch.randn(1000, 1))

# Set up the neural network, loss function and optimizer
model = SimpleNN()
criterion = nn.BCELoss()  # Binary Cross Entropy Loss
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Train the model
num_epochs = 25
for epoch in range(num_epochs):
    for i, (inputs, labels) in enumerate(zip(data.tensor().T, labels)):
        # Forward pass
        outputs = model(inputs.view(-1, 1))
        loss = criterion(outputs, labels.view(-1, 1))

        # Backward and optimization
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

# Testing the model on some None data
test_data = torch.tensor([[None]], dtype=torch.float)
outputs = model(test_data)
print('Prediction for None input:', outputs.item())
