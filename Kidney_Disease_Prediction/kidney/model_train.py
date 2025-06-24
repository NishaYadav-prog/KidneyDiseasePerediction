import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import pickle

data = pd.read_csv('Kidney_data.csv')  # Replace with full path if needed
print("Columns in the dataset:", data.columns)


# Load the data
data = pd.read_csv('Kidney_data.csv')  # Replace with full path if needed

# Handle missing values (if any) as described previously

# Convert categorical data to numeric using Label Encoding
label_encoder = LabelEncoder()
categorical_columns = ['column1', 'column2']  # Replace with actual categorical column names

for col in categorical_columns:
    data[col] = label_encoder.fit_transform(data[col])

# Encode the target variable
data['classification'] = label_encoder.fit_transform(data['classification'])

# Separate features and target
X = data.drop(['classification', 'id'], axis=1)  # Adjust columns as needed
y = data['classification']

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a model (e.g., Random Forest)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the model
with open('kidney_model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Model saved as kidney_model.pkl")
