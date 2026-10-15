
# Deep Learning and Machine Learning Practicals

This repository contains five Python-based practical implementations covering fundamental concepts of Machine Learning, Deep Learning, tensor operations, model training, and evaluation.

## Practicals Included

### 1. Tensor Manipulation
- Creates and manipulates tensors using PyTorch.
- Performs tensor addition, subtraction, and multiplication.
- Implements matrix multiplication, reshaping, indexing, and transpose.
- Calculates tensor mean and sum.

**Library:** PyTorch

### 2. Linear Regression
- Implements simple Linear Regression to predict house prices based on house size.
- Trains a regression model using sample data.
- Calculates slope and intercept.
- Evaluates the model using MSE and R² Score.
- Visualizes actual values and the regression line.

**Algorithm:** Linear Regression  
**Libraries:** NumPy, Matplotlib, Scikit-learn

### 3. Training Loop
- Implements a neural network training loop using PyTorch.
- Performs forward propagation.
- Calculates loss using Mean Squared Error (MSE).
- Performs backward propagation.
- Updates model weights using Stochastic Gradient Descent (SGD).
- Displays training loss across epochs.

**Framework:** PyTorch

### 4. Gradient Computation
- Demonstrates automatic differentiation using PyTorch Autograd.
- Computes gradients of mathematical functions.
- Uses `requires_grad=True` to track computations.
- Uses `backward()` to calculate derivatives.
- Explores gradient computation with multiple variables.

**Framework:** PyTorch

### 5. Model Evaluation
- Implements Linear Regression for model evaluation.
- Splits data into training and testing datasets.
- Evaluates model performance using different metrics.
- Calculates MAE, MSE, RMSE, and R² Score.
- Compares actual and predicted values.

**Algorithm:** Linear Regression  
**Library:** Scikit-learn

## Technologies Used

- Python 3
- PyTorch
- NumPy
- Pandas
- Matplotlib
- Scikit-learn

## Project Structure

```text
Deep-Learning-Practicals/
│
├── tensor_manipulation.py
├── linear_regression.py
├── training_loop.py
├── gradient_computation.py
├── model_evaluation.py
│
└── README.md
```

## Installation

Make sure Python 3 is installed on your system.

Install all required libraries:

```bash
pip install torch torchvision numpy pandas matplotlib scikit-learn
```

## How to Run

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the project directory:

```bash
cd Deep-Learning-Practicals
```

Execute individual Python programs:

```bash
python tensor_manipulation.py
```

```bash
python linear_regression.py
```

```bash
python training_loop.py
```

```bash
python gradient_computation.py
```

```bash
python model_evaluation.py
```

## Concepts Covered

- Tensor Creation and Manipulation
- Matrix Operations
- Linear Regression
- Neural Network Training
- Forward Propagation
- Backward Propagation
- Gradient Descent
- Automatic Differentiation
- Loss Functions
- Model Evaluation Metrics
- Prediction and Performance Analysis

## Learning Outcomes

After completing these practicals, you will understand:
- How tensors are created and manipulated using PyTorch.
- How Linear Regression works.
- How neural networks are trained using training loops.
- How gradients are calculated through automatic differentiation.
- How to evaluate machine learning models using performance metrics.

