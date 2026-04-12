def detect_anomalies(df, forecast_df):
    anomalies = []

    merged = df.copy()
    merged['yhat'] = forecast_df['yhat'][:len(df)].values
    merged['upper'] = forecast_df['yhat_upper'][:len(df)].values
    merged['lower'] = forecast_df['yhat_lower'][:len(df)].values

    for i, row in merged.iterrows():
        if row['y'] > row['upper'] or row['y'] < row['lower']:
            anomalies.append({
                "date": str(row['ds']),
                "value": float(row['y']),
                "reason": "Outside expected forecast range"
            })

    return anomalies