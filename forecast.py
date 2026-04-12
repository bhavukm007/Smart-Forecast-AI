from prophet import Prophet
import os  

def generate_forecast(df):
    model = Prophet(daily_seasonality=True)
    model.fit(df)

    periods = int(os.getenv("FORECAST_PERIODS", 30))

    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)

    return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]