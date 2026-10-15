
import torch
import torch.nn as nn
import torch.optim as optim

# Training dataset
X = torch.tensor([[1.0], [2.0], [3.0], [4.0], [5.0]])
y = torch.tensor([[2.0], [4.0], [6.0], [8.0], [10.0]])

# Create a linear model
model = nn.Linear(1, 1)

# Loss function
criterion = nn.MSELoss()

# Optimizer
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Training loop
epochs = 1000

for epoch in range(epochs):

    # Forward propagation
    predictions = model(X)

    # Calculate loss
    loss = criterion(predictions, y)

    # Clear previous gradients
    optimizer.zero_grad()

    # Backward propagation
    loss.backward()

    # Update weights
    optimizer.step()

    if (epoch + 1) % 100 == 0:
        print(f"Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}")

# Display trained parameters
print("\nTrained Weight:", model.weight.item())
print("Trained Bias:", model.bias.item())

# Test prediction
test = torch.tensor([[6.0]])

prediction = model(test)

print("\nPrediction for input 6:", prediction.item())
