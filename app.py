from flask import Flask, render_template, request
import pandas as pd
import os
from dotenv import load_dotenv

from forecast import generate_forecast
from baseline import baseline_forecast
from anomaly import detect_anomalies
from explanation import generate_explanation
from scenario import apply_scenario
from validation import validate_model

load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files.get('file')

    if not file:
        return "❌ No file uploaded"

    try:
        scenario_percent = float(request.form.get('scenario', 0))
    except:
        scenario_percent = 0

    scenario_mode = request.form.get('mode', 'growth')

    try:
        df = pd.read_csv(file)

        df.columns = [col.strip().lower() for col in df.columns]

        if 'date' not in df.columns or 'value' not in df.columns:
            return "❌ CSV must contain 'date' and 'value' columns"

        df = df[['date', 'value']]

        df.columns = ['ds', 'y']

        df['ds'] = pd.to_datetime(df['ds'], errors='coerce')

        if df['ds'].isnull().any():
            return "❌ Invalid date format in CSV"

        df = df.drop_duplicates(subset='ds')

        df = df.sort_values('ds')

        if df['y'].isnull().any():
            return "❌ Missing values detected in 'value' column"

        if len(df) < 10:
            return "❌ Dataset too small. Minimum 10 rows required."

    except Exception as e:
        return f"❌ Error processing file: {str(e)}"


    try:
        forecast_df = generate_forecast(df)

        baseline = baseline_forecast(df)

        accuracy = validate_model(df)

        anomalies = detect_anomalies(df, forecast_df)

        scenario_df = apply_scenario(forecast_df, scenario_percent, scenario_mode)

    except Exception as e:
        return f"❌ Model processing error: {str(e)}"

    forecast_df['ds'] = forecast_df['ds'].astype(str)
    scenario_df['ds'] = scenario_df['ds'].astype(str)

    explanation = generate_explanation(forecast_df, baseline, anomalies, accuracy)

    return render_template(
        'result.html',
        forecast=forecast_df.to_dict(orient='records'),
        scenario=scenario_df.to_dict(orient='records'),
        baseline=round(baseline, 2),
        anomalies=anomalies,
        explanation=explanation,
        accuracy=accuracy
    )

if __name__ == '__main__':
    app.run(debug=True)