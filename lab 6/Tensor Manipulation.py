
import torch

# Create tensors
a = torch.tensor([[1, 2], [3, 4]])
b = torch.tensor([[5, 6], [7, 8]])

print("Tensor A:")
print(a)

print("\nTensor B:")
print(b)

# Addition
print("\nAddition:")
print(a + b)

# Subtraction
print("\nSubtraction:")
print(a - b)

# Element-wise multiplication
print("\nElement-wise Multiplication:")
print(a * b)

# Matrix multiplication
print("\nMatrix Multiplication:")
print(torch.matmul(a, b))

# Reshaping
c = torch.arange(1, 10)
print("\nOriginal Tensor:")
print(c)

print("\nReshaped Tensor:")
print(c.reshape(3, 3))

# Indexing
print("\nElement at row 1, column 2:")
print(a[1, 0])

# Transpose
print("\nTranspose:")
print(a.T)

# Mean and sum
print("\nMean:", a.float().mean().item())
print("Sum:", a.sum().item())

# Tensor dimensions
print("\nShape:", a.shape)
print("Number of Dimensions:", a.ndim)
