from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/predict', methods=['POST'])
def predict():
    # ...existing code for prediction...
    return jsonify({'prediction': 'example_prediction'})

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'ok'}), 200
