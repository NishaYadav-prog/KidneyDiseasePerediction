# app.py

from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the saved model
with open('kidney_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract data from form
    input_features = [float(x) for x in request.form.values()]
    features_array = np.array([input_features])

    # Make prediction
    prediction = model.predict(features_array)
    output = 'Chronic Kidney Disease' if prediction[0] == 1 else 'No Chronic Kidney Disease'

    return render_template('index.html', prediction_text=f'Prediction: {output}')

if __name__ == '__main__':
    app.run(debug=True)
