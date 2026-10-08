
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Dataset
data = {
    'Income': [50000, 30000, 80000, 25000, 60000,
               90000, 35000, 70000, 45000, 100000,
               28000, 75000, 55000, 40000, 85000,
               32000, 95000, 48000, 65000, 38000],

    'LoanAmount': [20000, 25000, 30000, 18000, 25000,
                   40000, 22000, 35000, 20000, 45000,
                   15000, 30000, 28000, 18000, 38000,
                   17000, 42000, 24000, 32000, 19000],

    'CreditHistory': [1, 0, 1, 0, 1, 1, 0, 1, 1, 1,
                      0, 1, 1, 0, 1, 0, 1, 1, 1, 0],

    'Employment': ['Yes', 'No', 'Yes', 'No', 'Yes',
                   'Yes', 'No', 'Yes', 'Yes', 'Yes',
                   'No', 'Yes', 'Yes', 'No', 'Yes',
                   'No', 'Yes', 'Yes', 'Yes', 'No'],

    'LoanStatus': ['Approved', 'Rejected', 'Approved',
                   'Rejected', 'Approved', 'Approved',
                   'Rejected', 'Approved', 'Approved',
                   'Approved', 'Rejected', 'Approved',
                   'Approved', 'Rejected', 'Approved',
                   'Rejected', 'Approved', 'Approved',
                   'Approved', 'Rejected']
}

df = pd.DataFrame(data)

# Encode categorical data
encoder = LabelEncoder()

df['Employment'] = encoder.fit_transform(df['Employment'])
df['LoanStatus'] = encoder.fit_transform(df['LoanStatus'])

# Features and target
X = df[['Income', 'LoanAmount', 'CreditHistory', 'Employment']]
y = df['LoanStatus']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Feature scaling
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

# Predict for a new applicant
new_applicant = pd.DataFrame(
    [[65000, 25000, 1, 1]],
    columns=['Income', 'LoanAmount', 'CreditHistory', 'Employment']
)

new_applicant = scaler.transform(new_applicant)

prediction = model.predict(new_applicant)

if prediction[0] == 1:
    print("Loan Approved")
else:
    print("Loan Rejected")
