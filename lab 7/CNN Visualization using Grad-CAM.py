
import torch
import torch.nn.functional as F
import torchvision.models as models
import torchvision.transforms as transforms

import matplotlib.pyplot as plt
import numpy as np

from PIL import Image

# Load pretrained ResNet model
model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
model.eval()

# Select final convolutional layer
target_layer = model.layer4[-1]

# Store activations and gradients
activations = None
gradients = None

def forward_hook(module, input, output):
    global activations
    activations = output

def backward_hook(module, grad_input, grad_output):
    global gradients
    gradients = grad_output[0]

# Register hooks
target_layer.register_forward_hook(forward_hook)
target_layer.register_full_backward_hook(backward_hook)

# Image preprocessing
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

# Load image
image = Image.open("image.jpg").convert("RGB")
input_tensor = transform(image).unsqueeze(0)

# Forward pass
output = model(input_tensor)

predicted_class = output.argmax(dim=1).item()

# Backward pass
model.zero_grad()
score = output[0, predicted_class]
score.backward()

# Calculate Grad-CAM weights
weights = gradients.mean(dim=(2, 3), keepdim=True)

cam = (weights * activations).sum(dim=1)
cam = F.relu(cam)

# Normalize heatmap
cam = F.interpolate(
    cam.unsqueeze(1),
    size=(224, 224),
    mode='bilinear',
    align_corners=False
)

cam = cam.squeeze().detach().numpy()
cam = cam / (cam.max() + 1e-8)

# Display original image and heatmap
original = np.array(image.resize((224, 224)))

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.imshow(original)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(original)
plt.imshow(cam, cmap='jet', alpha=0.5)
plt.title("Grad-CAM Visualization")
plt.axis("off")

plt.tight_layout()
plt.show()
