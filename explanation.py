def generate_explanation(forecast_df, baseline, anomalies, accuracy):
    latest = forecast_df['yhat'].iloc[-1]
    first = forecast_df['yhat'].iloc[0]
    avg = forecast_df['yhat'].mean()

    trend_percent = ((latest - avg) / avg) * 100
    if trend_percent > 5:
        trend = "strong increasing"
    elif trend_percent > 0:
        trend = "slightly increasing"
    elif trend_percent < -5:
        trend = "declining"
    else:
        trend = "stable"

    if accuracy < 10:
        confidence = "High"
    elif accuracy < 20:
        confidence = "Moderate"
    else:
        confidence = "Low"

    explanation = f"""
📊 Forecast shows a {trend} trend ({round(trend_percent,2)}% change).

🔮 Predicted value: {round(latest,2)}
📉 Baseline: {round(baseline,2)}

📏 Model Accuracy (MAPE): {accuracy}%
🔐 Confidence Level: {confidence}

📌 Forecast range shows expected uncertainty band.
"""

    if anomalies:
        explanation += f"\n⚠️ {len(anomalies)} anomalies detected. Possible unusual events or spikes."

    explanation += "\n💡 Recommendation: Monitor anomalies and validate sudden changes before decisions."

    return explanation