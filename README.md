# Predictive Analysis for Manufacturing Operations

This is a simple Flask app that lets you upload data, train a model, and predict equipment downtime using temperature and runtime values.

## Features

1. **Upload Data**: You can upload a CSV file for training.
2. **Train Model**: Train a logistic regression model on the data.
3. **Make Predictions**: Use the trained model to predict downtime.

---

## Requirements

You need the following installed:

- Python 3.10 or higher
- Flask
- Pandas
- Scikit-learn
- Joblib

Install the required packages with:

```bash
pip install flask pandas scikit-learn joblib
```

---

## How to Use It

### 1. Start the App

Run this command:

```bash
python app.py
```

The app will start at `http://127.0.0.1:5000/`.

---

### 2. API Endpoints

#### **1. Upload Data**

- **URL**: `/upload`
- **Method**: `POST`
- **What It Does**: Uploads a CSV file.
- **Input Format**: The CSV file should have these columns:
  - `Temperature`
  - `Run_Time`
  - `Downtime_Flag`
- **Example cURL Command**:

```bash
curl -X POST -F "file=@your_dataset.csv" http://127.0.0.1:5000/upload
```

- **Response**:

```json
{
  "message": "Data uploaded successfully!",
  "columns": ["Temperature", "Run_Time", "Downtime_Flag"]
}
```

#### **2. Train Model**

- **URL**: `/train`
- **Method**: `POST`
- **What It Does**: Trains a logistic regression model.
- **Example cURL Command**:

```bash
curl -X POST http://127.0.0.1:5000/train
```

- **Response**:

```json
{
  "accuracy": 0.9,
  "f1_score": 0.8,
  "message": "Model trained successfully!"
}
```

#### **3. Predict Downtime**

- **URL**: `/predict`
- **Method**: `POST`
- **What It Does**: Predicts downtime based on input values.
- **Input Format (JSON)**:

```json
{
  "Temperature": 70,
  "Run_Time": 120
}
```

- **Example cURL Command**:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"Temperature": 60, "Run_Time": 200}' http://127.0.0.1:5000/predict
```

- **Response**:

```json
{
  "Confidence": 0.89,
  "Downtime": "No"
}
```
- **Example cURL Command**:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"Temperature": 50, "Run_Time": 50}' http://127.0.0.1:5000/predict
```

- **Response**:

```json
{
  "Confidence": 0.83,
  "Downtime": "Yes"
}
```

---

## Project Files

```
.
├── app.py                # Main app file
├── model.pkl             # Saved trained model
├── sample_dataset.csv      # Dependencies
├── utils.py              # To generate sample dataset 
```

---

## Notes

- Make sure your CSV file has the correct columns.
- The trained model is saved as `model.pkl`.
- Predictions include a confidence score from the model.

---

## Future Plans

1. Add more machine learning models.
2. Create data visualization tools.
3. Add automatic parameter tuning.

---
