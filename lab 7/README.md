# Deep Learning and Machine Learning Practicals

This repository contains Python implementations of **Grad-CAM Visualization** and **Model Evaluation using Linear Regression**. These practicals demonstrate model interpretability and evaluation techniques using popular machine learning and deep learning libraries.

## 📂 Practical List

| No. | Practical | Description |
|---|---|---|
| 1 | CNN Visualization using Grad-CAM | Visualizes important image regions influencing a CNN's prediction using Grad-CAM and ResNet18. |
| 2 | Model Evaluation | Evaluates a Linear Regression model using MAE, MSE, RMSE, and R² score. |

## 🛠️ Technologies Used

- Python 3
- PyTorch
- Torchvision
- NumPy
- Matplotlib
- Pillow (PIL)
- Scikit-learn

## 📁 Project Structure

```text
Deep-Learning-Practicals/
│
├── CNN Visualization using Grad-CAM.py
├── Model Evaluation.py
├── image.jpg
└── README.md
```

**Note:** `image.jpg` is required for the Grad-CAM practical. Place an image in the same directory as the Python file.

## ⚙️ Installation

Install the required libraries:

```bash
pip install torch torchvision numpy matplotlib pillow scikit-learn
```

## ▶️ How to Run

### 1. CNN Visualization using Grad-CAM

```bash
python "CNN Visualization using Grad-CAM.py"
```

**Concepts Covered:**
- Convolutional Neural Networks (CNN)
- Pretrained ResNet18 architecture
- Forward and backward hooks
- Activation and gradient extraction
- Grad-CAM heatmap generation
- Image visualization using Matplotlib

**Working:**
1. Loads a pretrained ResNet18 model.
2. Loads and preprocesses the input image.
3. Performs a forward pass to predict the image class.
4. Extracts activations and gradients from the final convolutional layer.
5. Calculates Grad-CAM weights and generates a heatmap.
6. Displays the original image alongside the Grad-CAM visualization.

**Output:** Displays the original image and a heatmap highlighting regions that contribute to the model's prediction.

*The pretrained ResNet18 weights may be downloaded automatically during the first execution.*

### 2. Model Evaluation

```bash
python "Model Evaluation.py"
```

**Concepts Covered:**
- Linear Regression
- Training and testing datasets
- Model prediction
- Regression evaluation metrics
- Actual vs. predicted value comparison

**Working:**
1. Creates a sample dataset containing input and target values.
2. Splits the dataset into training and testing sets.
3. Trains a Linear Regression model.
4. Predicts output values using the test dataset.
5. Evaluates the model using four performance metrics.
6. Displays actual and predicted values.

**Evaluation Metrics:**

| Metric | Description |
|---|---|
| MAE | Mean Absolute Error |
| MSE | Mean Squared Error |
| RMSE | Root Mean Squared Error |
| R² Score | Measures how well the model explains variations in the target values. |

## 🎯 Learning Outcomes

After completing these practicals, you will understand:

- How to visualize CNN model predictions using Grad-CAM.
- How pretrained ResNet18 models perform image classification.
- How forward and backward hooks capture activations and gradients.
- How to train and test a Linear Regression model.
- How to evaluate regression models using standard performance metrics.
- How to compare actual and predicted values.