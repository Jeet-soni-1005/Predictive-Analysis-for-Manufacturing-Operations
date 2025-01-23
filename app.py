from flask import Flask, request, jsonify
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
import joblib

app = Flask(__name__)

# Global variables to hold data and model
uploaded_data = None
model = None

@app.route('/upload', methods=['POST'])
def upload_data():
    global uploaded_data
    file = request.files['file']
    if file:
        uploaded_data = pd.read_csv(file)
        return jsonify({"message": "Data uploaded successfully!", "columns": uploaded_data.columns.tolist()})
    return jsonify({"error": "No file uploaded"}), 400

@app.route('/train', methods=['POST'])
def train_model():
    global uploaded_data, model
    if uploaded_data is None:
        return jsonify({"error": "No data uploaded. Please upload data first."}), 400

    # Prepare data
    X = uploaded_data[['Temperature', 'Run_Time']]
    y = uploaded_data['Downtime_Flag']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Evaluate model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    # Save the model
    joblib.dump(model, 'model.pkl')

    return jsonify({"message": "Model trained successfully!", "accuracy": accuracy, "f1_score": f1})

@app.route('/predict', methods=['POST'])
def predict():
    global model
    if model is None:
        return jsonify({"error": "Model not trained. Please train the model first."}), 400

    # Parse input
    data = request.json
    if not all(k in data for k in ('Temperature', 'Run_Time')):
        return jsonify({"error": "Missing required input fields: 'Temperature' and 'Run_Time'"}), 400

    X_new = [[data['Temperature'], data['Run_Time']]]
    prediction = model.predict(X_new)
    confidence = max(model.predict_proba(X_new)[0])

    return jsonify({"Downtime": "Yes" if prediction[0] == 1 else "No", "Confidence": round(confidence, 2)})

if __name__ == '__main__':
    app.run(debug=True)
