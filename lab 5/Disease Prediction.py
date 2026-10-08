
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# Dataset
data = {
    'Glucose': [120, 85, 150, 90, 180, 110, 160, 95, 140, 100,
                170, 80, 155, 105, 190, 115, 145, 88, 165, 98],
    'BMI': [32, 22, 35, 24, 38, 28, 36, 21, 33, 25,
            37, 20, 34, 27, 40, 29, 31, 23, 39, 26],
    'Age': [45, 25, 50, 30, 55, 35, 48, 28, 52, 32,
            58, 22, 46, 38, 60, 40, 49, 26, 56, 31],
    'Diabetes': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0,
                 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
}

df = pd.DataFrame(data)

# Features and target
X = df[['Glucose', 'BMI', 'Age']]
y = df['Diabetes']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Train model
model = DecisionTreeClassifier(
    criterion='entropy', max_depth=3, random_state=42
)
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

# Predict for a new person
new_person = pd.DataFrame(
    [[140, 32, 45]],
    columns=['Glucose', 'BMI', 'Age']
)

prediction = model.predict(new_person)

if prediction[0] == 1:
    print("Model predicts diabetes.")
else:
    print("Model predicts no diabetes.")
