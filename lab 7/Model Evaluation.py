
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# Dataset
X = np.array([
    [500], [600], [700], [800], [900],
    [1000], [1100], [1200], [1300], [1400],
    [1500], [1600], [1700], [1800], [1900],
    [2000], [2100], [2200], [2300], [2400]
])

y = np.array([
    10, 12, 14, 16, 18,
    20, 22, 24, 26, 28,
    30, 32, 34, 36, 38,
    40, 42, 44, 46, 48
])

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

# Display results
print("Model Evaluation Results")

print("------------------------")
print("Mean Absolute Error (MAE):", mae)
print("Mean Squared Error (MSE):", mse)
print("Root Mean Squared Error (RMSE):", rmse)
print("R2 Score:", r2)

# Compare actual and predicted values
print("\nActual vs Predicted")

for actual, predicted in zip(y_test, y_pred):
    print(f"Actual: {actual}, Predicted: {predicted:.2f}")
