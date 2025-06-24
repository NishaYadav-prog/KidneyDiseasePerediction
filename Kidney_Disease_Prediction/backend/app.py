from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
# Load the trained model
model = joblib.load('kidney_disease_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json  # Get data from the request body
    # Extract the relevant features
    features = np.array([data['age'], data['bp'], data['sg'], data['al'], data['glucose']])
    
    # Make the prediction using the model
    prediction = model.predict([features])
    
    # Return the prediction result
    result = 'Kidney Disease' if prediction[0] == 1 else 'No Kidney Disease'
    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)
