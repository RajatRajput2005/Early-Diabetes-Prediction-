import sys
import joblib
import numpy as np

# Load the model and scaler
model = joblib.load('diabetes_model.pkl')
scaler = joblib.load('scaler.pkl')

# Get input data from command-line arguments
age = float(sys.argv[1])
gender = int(sys.argv[2])
bmi = float(sys.argv[3])
smoking_history = int(sys.argv[4])
hba1c_level = float(sys.argv[5])
blood_glucose_level = float(sys.argv[6])

# Scale the input data
input_data = scaler.transform([[age, smoking_history, bmi, hba1c_level, blood_glucose_level]])
input_data = np.insert(input_data, 1, gender, axis=1)  # Insert gender into the scaled data

# Make prediction
prediction = model.predict(input_data)
result = 'Diabetic' if prediction[0] == 1 else 'Non-Diabetic'

print(result)
