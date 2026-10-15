
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Dataset: House size and price
# Price is in lakhs
X = np.array([
    [500], [700], [800], [1000],
    [1200], [1500], [1800], [2000]
])

y = np.array([15, 20, 22, 28, 32, 40, 48, 52])

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Predictions
y_pred = model.predict(X)

# Model parameters
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)

# Evaluation
print("\nMean Squared Error:",
      mean_squared_error(y, y_pred))

print("R2 Score:", r2_score(y, y_pred))

# Predict price for a new house
new_house = np.array([[1300]])
predicted_price = model.predict(new_house)

print("\nPredicted Price for 1300 sq.ft:",
      predicted_price[0], "Lakhs")

# Visualization
plt.scatter(X, y, color='blue', label='Actual Prices')
plt.plot(X, y_pred, color='red', label='Regression Line')

plt.xlabel("House Size (sq.ft)")
plt.ylabel("Price (Lakhs)")
plt.title("Linear Regression")
plt.legend()
plt.show()
