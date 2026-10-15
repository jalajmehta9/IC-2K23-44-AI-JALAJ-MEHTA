
import torch

# Create a tensor with gradient tracking
x = torch.tensor(3.0, requires_grad=True)

# Define mathematical function
# y = x^2 + 3x + 2
y = x**2 + 3*x + 2

# Display function value
print("Value of y:", y.item())

# Compute gradient
y.backward()

# Display gradient
print("Gradient dy/dx:", x.grad.item())

# Another example using multiple variables
a = torch.tensor(2.0, requires_grad=True)
b = torch.tensor(4.0, requires_grad=True)

# Function: z = a^2 + b^2 + a*b
z = a**2 + b**2 + a*b

# Compute gradients
z.backward()

print("\nValue of z:", z.item())
print("Gradient dz/da:", a.grad.item())
print("Gradient dz/db:", b.grad.item())
