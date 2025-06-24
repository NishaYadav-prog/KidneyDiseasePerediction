import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load dataset (You can download CKD dataset from UCI or Kaggle)
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00344/Chronic_Kidney_Disease/chronic_kidney_disease_full.arff'

# Preprocessing the dataset
def load_and_process_data():
    data = pd.read_csv(url)  # assuming you've saved or accessed the dataset
    data.fillna(method='ffill', inplace=True)  # handling missing data
    data['class'] = data['class'].map({'ckd': 1, 'notckd': 0})  # convert target to 0, 1
    X = data.drop(columns=['class'])
    y = data['class']
    return train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
def train_and_save_model():
    X_train, X_test, y_train, y_test = load_and_process_data()
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model accuracy: {accuracy * 100:.2f}%")
    
    # Save the model
    joblib.dump(model, 'kidney_disease_model.pkl')
    print("Model saved!")

if __name__ == '__main__':
    train_and_save_model()
