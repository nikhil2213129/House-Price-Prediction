import pickle
from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the model
model = joblib.load('House_Price_Prediction.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    print(data)  # For debugging purposes

    try:
        prediction = model.predict(data)
        return jsonify({'prediction': prediction.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
